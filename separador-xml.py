import os
import shutil
import xml.etree.ElementTree as ET

# Caminho onde os XML estão
CAMINHO_XML = r"C:\Users\Dayane\Downloads\XML"

# Caminho onde os XML separados serão salvos
DESTINO = os.path.join(CAMINHO_XML, "Separados")

def garantir_pasta(path):
    """Cria a pasta caso não exista"""
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def extrair_cnpj(xml_path):
    """Extrai o CNPJ do XML de forma segura"""
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        cnpj_tag = root.find(".//{http://www.portalfiscal.inf.br/nfe}CNPJ")
        return cnpj_tag.text if cnpj_tag is not None else None
    except:
        return None

def mover_por_cnpj():
    """Processa e organiza os arquivos XML por CNPJ"""
    garantir_pasta(DESTINO)

    for arquivo in os.listdir(CAMINHO_XML):
        if not arquivo.lower().endswith(".xml"):
            continue

        caminho_xml = os.path.join(CAMINHO_XML, arquivo)
        print(f"📄 Processando: {arquivo}")

        cnpj = extrair_cnpj(caminho_xml)

        if cnpj:
            pasta_destino = garantir_pasta(os.path.join(DESTINO, cnpj))
        else:
            pasta_destino = garantir_pasta(os.path.join(DESTINO, "Sem-CNPJ"))

        shutil.move(caminho_xml, os.path.join(pasta_destino, arquivo))
        print(f"✔ Movido para: {pasta_destino}\n")

    print("\n🎉 Finalizado! XML separados com sucesso.")

if __name__ == "__main__":
    mover_por_cnpj()
