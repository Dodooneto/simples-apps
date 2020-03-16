#apresentação
print("=====================================================================================================================")                 
print ("==================================== PROGRAMA  DE  ORG.  DE  NOTAS ==================================================")
print("=====================================================================================================================")
print("---------------------------------------------------------------------------------------------------")
print("by:Dodo") 
print("---------------------------------------------------------------------------------------------------") 
print("2020")
print("---------------------------------------------------------------------------------------------------")
print("Se minha Teoria da Relatividade estiver correta,")
print("a Alemanha dirá que sou alemão e a França um cidadão do mundo. Mas, se não estiver,")
print("a França dirá que sou alemão e os alemães dirão que sou judeu.")
print("                                                                 ""Albert Einstein")
print("---------------------------------------------------------------------------------------------------")
#mysql, exit e temporizador
import pymysql

import time
import sys
conexão= pymysql.connect( db="ControledeNotas", user="root", passwd='rootpassword')
cursor = conexão.cursor()

def linha():
    print("-----------------")

def espaço():
    print("     ")
    print("     ")

def inf_adicionar():
    adc=int(input("(1)Cadastrar novo aluno ?, (2)adicionar notas de alunos ou (3)adicionar pontos de professor ?: "))
    espaço()
    if adc==1:
        nomedonovoaluno=input("Nome do novo aluno ?: ")
        espaço()
        print("Modelo[ 3 E.M ou 3 E.F]")
        espaço()
        time.sleep(1)
        seriedoalunonovo=input("Série do novo aluno ?: ")
        espaço()
        if type(nomedonovoaluno)== str and type(seriedoalunonovo)== type("3 E.M"):
            cursor.execute("INSERT INTO historicoescolar(aluno, serie) VALUES ('"+nomedonovoaluno+"', '"+seriedoalunonovo+"')");
            print("Informações adicionadas com sucesso ")
            conexão.commit() 
            espaço()
            firsway()
        else:
            print("Erro ao adicionar, tente novamente ")
            espaço()
            time.sleep(1)
            firsway()    
    elif adc== 2:
        nomedoaluno=input("Qual o nome do aluno ?: ")
        espaço()
        serie=input("Série atual ?: ")
        espaço() 
        numero_de_materias=int(input("Qual o número de matérias que seráo alteradas ?: "))
        i=1
        espaço()
        while i<=numero_de_materias  :
            inf=input("Adicionar nota de qual matéria ?: ")                                                                                               
            espaço()
            tri=int(input("Qual trimestre ?: "))
            espaço()
            prova=int(input("Qual prova ?: ")) 
            i=i+1 
            espaço()
            nota=(input("Nota ?: "))
            if type(inf)== str and type(tri)== int and type(prova)== int and type(nota)== type("9.02") :
                cursor.execute("UPDATE historicoescolar('+inf+', trimestre, n_prova) SET('nota', 'tri', 'prova') WHERE aluno='"+nomedoaluno+"' and serie='"+serie+"'")       
                print("Informações adicionadas com sucesso ")
                conexão.commit() 
            else:
                print("Erro ao adicionar, tente novamente ")    
                return   
        espaço()
        time.sleep(1)
        inf_adicionar()

    elif adc== 3:
        nomedoaluno=input("Qual o nome do aluno ?: ")
        espaço()
        serie=input("Série atual ?: ")
        espaço() 
        tri=int(input("Qual trimestre ?: "))
        notas_professores=input("Adicionar 'ponto de professor' de qual matéria ?: ")
        cursor.execute("UPDATE historicoescolar(notasdeprof,trimestre) SET ('"+notas_professores+"', '"+tri+"') WHERE aluno='"+nomedoaluno+"' and serie='"+serie+"'")
        espaço()
        time.sleep(1)
        inf_adicionar()

        
    else:
        print("Opção inexistente")
        firsway()
                      
def consultar_boletim(): 
    consulta=input ("Consultar boletim anual ou trimestral ?: ")
    nomealuno=input ("Qual o nome do aluno ?: ")
    consulta=consulta.lower()      
    if consulta=="anual":
        serie=input("Histórico de qual turma ?: ")
        cursor.execute("SELECT aluno, serie, notasfinais FROM historicoescolar WHERE aluno='"+nomealuno+"' and serie='"+serie+"'");
        resultado=cursor.fetchone()
        for result in resultado :
            print ("------------------")
            print ("----",result,"----")
            print ("------------------")
    elif consulta=="trimestral":
        trimestre=input("Qual trimestre ?: ")
        serie_2=input("Histórico do trimestre de qual turma ?: ")
        cursor.execute("SELECT aluno, serie, trimestre, ingles, matematica, portugues, geografia, historia, filosofia, sociologia, quimica, biolla, fisica FROM histdealu WHERE aluno='"+nomealuno+"' and trimestre='"+trimestre+"' and serie='"+serie_2+"'")
        resultado2=cursor.fetchone()
        for result2 in resultado2:
            print ("-------------------")
            print ("----",result2,"----")
            print ("-------------------")

def firsway():
    primeirocaminho=int(input("Olá, deseja (1)adicionar, (2)consultar ou (3)deletar informações ?: "))
    espaço()
    if primeirocaminho == 1:   
        inf_adicionar()
    elif primeirocaminho == 2:
        consultar_boletim()
    elif primeirocaminho == 3:
        inf_deletar()
    else:
        print("Opção inválida! ")
        espaço()
        print("Tente novamente: ")
        espaço()
        firsway()

def inf_deletar():
    nomealuno=input("Deletar informações de qual aluno ?: ")
    espaço()
    cursor.execute("DELETE FROM  histdealu where aluno='"+nomealuno+"'")
    conexão.commit()
    time.sleep(1)
    print("Deletado com sucesso")
    espaço()
    espaço()
    time.sleep(1)
    firsway()

def fim_end():
    fim=input("Gostaria fazer algo mais ?: ")
    espaço()
    time.sleep(1)
    fim=fim.lower()
    if fim=="sim":
        firsway()
    elif fim=="não":
        sys.exit()
    else:
        print("Opção inválida! ")
        espaço()
        print("Tente novamente: ")
        espaço()
        time.sleep(1)
        fim_end()

firsway()


    
