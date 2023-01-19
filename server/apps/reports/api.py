"""
API Relatórios

Sobre-escrita das chamadas base da API

"""
import os
import uuid
from datetime import datetime
from pytz import timezone
import pandas
from flask import jsonify
from server.driver import db
from server.api import BaseApi
from .models import Report

class ReportApi(BaseApi):
    """
    API relatórios

    """
    model = Report
    collection = "reports"
    methods = ["list", "retrieve", "create"]

    def create(self, data):
        """
        API para criação de relatórios

        """

        report_id = uuid.uuid4().hex
        group_id = data["group_id"]

        # Obtendo sensores do grupo
        query_sensors = db().sensors.find({"group_id": {"$in": group_id}}, {"_id": 1, "group_id": 1})
        sensors = [(sensor["_id"], sensor["group_id"])
                       for sensor in query_sensors]  # Lista de IDs e Grupos dos sensores
        sensors = list(zip(*sensors))
        sensors_ids  = list(sensors[0])
        sensors_groups = list(sensors[1])

        if not sensors:
            return f"Nenhum sensor dos grupos {group_id} foi encontrado", 404

        # Obtendo leituras
        query_docs = db().reads.find({"parent_id": {"$in": sensors_ids}})

        # Cada documento do db deverá ser uma linha na tabela
        lines = []
        for doc in query_docs:

            data = [
                sensors_groups[sensors_ids.index(doc["parent_id"])],
                doc["parent_id"],
                doc["value"],
                doc["reliable"]
            ]

            lines.append(list(pandas.Series(data)))

        # Definindo tabela
        report = pandas.DataFrame(lines, columns=["Grupo do sensor",
                                                  "Identificador do sensor",
                                                  "Valor da leitura",
                                                  "Confiabilidade da leitura"],)

        # Divisão do dataframe para geração de gráficos
        for group in group_id:
            pass

        # Definindo pasta em que os relatórios serão salvos
        folder_dir = os.path.join(os.getcwd(),
                                  "bucket",
                                  "reports",
                                  report_id)

        # Caso a pasta não exista, é necessário criá-la
        os.makedirs(folder_dir, exist_ok=True)

        # Obtendo hora atual para nomear arquivo
        local_time = datetime.now().astimezone(timezone('America/Sao_Paulo'))
        timestamp = local_time.strftime('%d-%m-%y_%H-%M-%S')
        file_path = os.path.join(
            folder_dir, f"Relatorio-{group_id}-{timestamp}")

        # Transformando dataframe em arquivo .csv e salvando na pasta
        report.to_csv(f"{file_path}.csv")

        # Adicionando arquivos no objeto do db
        files = [
            f"/api/files/{report_id}/Relatorio-{group_id}-{timestamp}.csv"
        ]
        doc_data = dict(_id=report_id, files=files)
        
        db().reports.insert_one(doc_data)

        return jsonify(doc_data), 200
