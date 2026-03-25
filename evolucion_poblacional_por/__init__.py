"""Dataset demografico longitudinal con estructura de edad de la poblacion para 11 paises de America La
DOI: https://github.com/juanmoisesd/evolucion-poblacional-por-grupos-de-edad-en-america-latina-2000-2023-dataset-dem | GitHub: https://github.com/juanmoisesd/evolucion-poblacional-por-grupos-de-edad-en-america-latina-2000-2023-dataset-dem"""
__version__="1.0.0"
__author__="de la Serna, Juan Moisés"
import pandas as pd,io
try:
    import requests
except ImportError:
    raise ImportError("pip install requests")

def load_data(filename=None):
    """Load dataset from Zenodo. Returns pandas DataFrame."""
    rid="https://github.com/juanmoisesd/evolucion-poblacional-por-grupos-de-edad-en-america-latina-2000-2023-dataset-dem".split(".")[-1]
    meta=requests.get(f"https://zenodo.org/api/records/{rid}",timeout=30).json()
    csvs=[f for f in meta.get("files",[]) if f["key"].endswith(".csv")]
    if not csvs:raise ValueError("No CSV found")
    f=next((x for x in csvs if filename and x["key"]==filename),csvs[0])
    return pd.read_csv(io.StringIO(requests.get(f["links"]["self"],timeout=60).text))

def cite():return f'de la Serna, Juan Moisés (2025). Dataset demografico longitudinal con estructura de edad de la poblacion para 11 . Zenodo. https://github.com/juanmoisesd/evolucion-poblacional-por-grupos-de-edad-en-america-latina-2000-2023-dataset-dem'
def info():print(f"Dataset: Dataset demografico longitudinal con estructura de edad de la poblacion para 11 \nDOI: https://github.com/juanmoisesd/evolucion-poblacional-por-grupos-de-edad-en-america-latina-2000-2023-dataset-dem\nGitHub: https://github.com/juanmoisesd/evolucion-poblacional-por-grupos-de-edad-en-america-latina-2000-2023-dataset-dem")