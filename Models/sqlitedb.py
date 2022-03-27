import sqlite3

class pesquisadb:

    def criar_banco_tabela():
        conectar = sqlite3.connect('pesquisa.db')
        cursor = conectar.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS voto (
	    id varchar(255),
	    voto_sim bool,
	    voto_nao bool,
        nao_opinou bool,
	    PRIMARY KEY(id));''')
        conectar.commit()
        conectar.close()

    def computar_voto(idn, voto_sim, voto_nao, nao_opinou):
        conectar = sqlite3.connect('pesquisa.db')
        cursor = conectar.cursor()
        cursor.execute('''
        INSERT INTO voto (id, voto_sim, voto_nao, nao_opinou)
        VALUES ({},{},{},{});'''.format(idn, voto_sim, voto_nao, nao_opinou))
        conectar.commit()
        conectar.close()

    def contagem_sim():
        conectar = sqlite3.connect('pesquisa.db')
        cursor = conectar.cursor()
        valor = cursor.execute('''
        select count (*) from voto where voto_sim = '1';''')
        resultado = (valor.fetchone()[0])
        return resultado

    def contagem_nao():
        conectar = sqlite3.connect('pesquisa.db')
        cursor = conectar.cursor()
        valor = cursor.execute('''
        select count (*) from voto where voto_nao = '1';''')
        resultado = (valor.fetchone()[0])
        return resultado

    def contagem_sem_voto():
        conectar = sqlite3.connect('pesquisa.db')
        cursor = conectar.cursor()
        valor = cursor.execute('''
        select count (*) from voto where nao_opinou = '1';''')
        resultado = (valor.fetchone()[0])
        return resultado

    def contagem_pessoas():
        conectar = sqlite3.connect('pesquisa.db')
        cursor = conectar.cursor()
        valor = cursor.execute('''
        select count (*) from voto where id != '0';
        ''')
        resultado = (valor.fetchone()[0])
        return resultado


