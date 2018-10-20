# -*- coding: utf-8 -*-

# Projecto
# Criar programa que permite analisar o estado de saúde dos pacientes mediantes 
# os valores de vários dados fisiológicos e biométricos:
# idade, género, altura, peso, ritmo cardíaco médio (semana), tensão arterial, 
# glicose no sangue, calorias ingeridas por semana (média).

#------------------------------#
#       Main Function          #
#------------------------------#
def main():
    patients = load_patients()
    
    while True:
        show_main_menu()
        option = input('Opção: ')
        
        options = {
            '1': list_patients,
            '2': insert_patient,
            '3': check_patient,
            '4': delete_patient,
            '5': statistics,
        }
        if option.lower() != 's':
            func = options.get(option, lambda x: print('('+option+') é um comando desconhecido!!'))
            func(patients)
        else:
            break;
            
    save = input('Deseja guardar os dados (s/n)? ')
    if save == 's':
        write_file_data(patients)
        
    exit

#------------------------------#
#  1st Level Menu Functions    #
#------------------------------#
def show_main_menu():
    print("\nClínica do Padre Amaro")
    print('Menu')
    print('(1) Listar pacientes')
    print('(2) Inserir paciente')
    print('(3) Avaliar paciente')
    print('(4) Eliminar paciente')
    print('(5) Estatísticas')
    print('(S) Sair')
    
def list_patients(patients):
    print('list_patients')
    # Write your code here...
    
def insert_patient(patients):
    name = input('Nome: ')
    gender = input('Género: ')
    age = input('Idade: ')
    weight = input('Peso: ')
    height = input('Altura: ')
    h_rhythm = input('Ritmo Cardíaco: ')
    h_tension = input('Tensão arterial: ')
    glucose = input('Glucose no sangue (mg/dl): ')
    cal = input('Calorias ingeridas (kcal/semana): ')
    
    pid = str(int(patients[-1]['id'])+1)
    last_patient = {
        'id': pid, 
        'name': name,
        'gender': gender,
        'age': age,
        'weight': weight,
        'height': height,
        'h_rhythm': h_rhythm, 
        'h_tension': h_tension, 
        'glucose': glucose, 
        'cal': cal
    }
    patients.append(last_patient)
    
def check_patient(patients):
    pid = input('ID do paciente: ')
    patient = load_patient(patients, pid)
    
    while patient != -1 and True:
        show_patient_submenu(patient['name'])
        option = input('Opção: ')
        
        options = {
            '1': check_obesity,
            '2': check_diabetes,
            '3': check_calory_intake,
        }
        if option.lower() != 'v':
            func = options.get(option, lambda x: print('('+option+') é um comando desconhecido'))
            func(patient)
        else:
            break;
    
def delete_patient(patients):
    pid = input('ID do paciente: ')
    print(patients[0]['id'])
    for i in range(len(patients)):
        if patients[i]['id'] == pid:
            del patients[i]
            break

def statistics(patients):
    print('statistics')
    # Write your code here...
    
#------------------------------#
#  2nd Level Menu Functions    #
#------------------------------#
def show_patient_submenu(patient_name):
    print("\nClínica do Padre Amaro")
    print('-> Avaliar paciente: '+patient_name)
    print('(1) Diagnóstico obesidade')
    print('(2) Diagnóstico diabetes')
    print('(3) Verificação calorias semanais')
    print('(V) Voltar')
    
def check_obesity(patient):
    print('check_obesity')
    # Write your code here...
    
def check_diabetes(patient):
    print('check_diabetes')
    # Write your code here...
    
def check_calory_intake(patient):
    print('check_calory_intake')
    # Write your code here...
        
#------------------------------#
#       Extra Functions        #
#------------------------------#
    
def load_patients():
    data = read_file_data('dataset_pacientes.csv')
    patients = []
    for line in data:
        patient = {}
        id, name, gender, age, weight, height, h_rhythm, h_tension, glucose, cal = line.split(sep=',')
        patient['id'] = id
        patient['name'] = name
        patient['gender'] = gender
        patient['age'] = age
        patient['weight'] = weight
        patient['height'] = height
        patient['h_rhythm'] = h_rhythm
        patient['h_tension'] = h_tension
        patient['glucose'] = glucose
        patient['cal'] = cal
        
        patients.append(patient)
        
    return patients

def load_patient(patients, pid):
    for patient in patients:
        if patient['id'] == pid:
            return patient
    return -1

def load_calorie_intake_data():
    data = read_file_data('calorie_intake.csv')
    cal_data = []
    for line in data:
        line = line.replace('\n', '').split(',')
        cal_data.append(line)
        
    return cal_data

def read_file_data(filepath):
    f = open(filepath, 'r')
    f.readline() # Remove 1st line which is data header
    data = f.readlines()
    f.close()
    
    return data

def write_file_data(data):
    f = open('dataset_pacientes.csv', 'w')
    lines = []
    for line in data:
        l = ','.join([val for (key,val) in line.items()])
        lines.append(l)
    
    lines.insert(0, 'id,name,gender,age,weight (kg),height (m),hearth rhythm (bpm),blood pressure,glucose level (fasting)(mg/dl),calorie intake (week)')
    f.writelines(lines)
    f.close()

def calculate_imc(weight, height):
    print('calculate_imc')
    # Write your code here...

# Run program
main()