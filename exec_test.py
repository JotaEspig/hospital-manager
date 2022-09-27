from config.config import db
from tests import admin
from tests import doenca
from tests import exame
from tests import hospital
from tests import paciente
from tests import remedio


def main() -> None:
    print("== Teste de Admin ==")
    admin.test_admin()
    print("\n== Teste de Doença ==")
    doenca.test_doenca()
    print("\n== Teste de Exame ==")
    exame.test_exame()
    print("\n== Teste de Hospital ==")
    hospital.test_hospital()
    print("\n== Teste de Paciente ==")
    paciente.test_paciente()
    print("\n== Teste da Remédio ==")
    remedio.test_remedio()
    

if __name__ == "__main__":
    db.create_all()
    main()
