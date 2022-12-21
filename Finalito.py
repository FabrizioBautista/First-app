import streamlit as st
import pandas as pd
import numpy as np

lista = ['fbautistaca@unsa.edu.pe']
if st.experimental_user.email in lista:
    st.write('Welcome', st.experimental_user.email)
    

menu = st.sidebar.markdown("<h2 style='text-align: ; color: black;'>Menu</h2>", unsafe_allow_html=True)
inicio = st.sidebar.button('Inicio')
objetivos = st.sidebar.button('Objetivos')
base_teorica = st.sidebar.button('Base Teorica')
propuesta = st.sidebar.button('Propuesta')
correlacion_de_pearson = st.sidebar.button('Correlacion de Pearson')
nuestra_correlacion = st.sidebar.button('Nuestra Correlacion')
mapa_de_calor = st.sidebar.button('Mapa de Calor')
validacion_de_resultados = st.sidebar.button('Validacion de Resultados')
conclusiones = st.sidebar.button('Conclusiones')
st.snow()
st.balloons()
if inicio:
    st.snow()
    st.markdown("<h2 style='text-align: center; color: black;'>Universidad Nacional de San Agustín de Arequipa </h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black;'>Escuela Profesional de Ingeniería de Telecomunicaciones </h2>", unsafe_allow_html=True)

    st.image('https://www.unsa.edu.pe/wp-content/uploads/sites/3/2018/05/Logo-UNSA.png')

    st.markdown("<h2 style='text-align: center; color: black;'>Ingeniero Renzo Bolivar - Docente DAIE </h2>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center; color: black;'>Curso : Computación 1 </h2>", unsafe_allow_html=True)

    st.image('https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png')

    st.markdown("<h2 style='text-align: center; color: black;'>GRUPO A - Nº4 </h2>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center; color: black;'>Alumnos:</h2>", unsafe_allow_html=True) 

    st.markdown("<h2 style='text-align: center; color: black;'>Alanoca Maquera, Brandon Yoel</h2>", unsafe_allow_html=True)   
    st.markdown("<h2 style='text-align: center; color: black;'>Bautista Cari, Fabrizio Miguel</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black;'>Sarcco Yana Jose, Fabricio</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black;'>Pacco Chua Yaseth, Yeremi</h2>", unsafe_allow_html=True)           
    st.markdown("<h2 style='text-align: center; color: black;'>Miranda Cahuana, Francisco Alonso</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black;'>Yanqui Calcina, Hierald Farid</h2>", unsafe_allow_html=True)

    st.image('https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png')

    st.markdown("<h2 style='text-align: center; color: black;'>INVESTIGACIÓN FORMATIVA</h2>", unsafe_allow_html=True)
  
    st.markdown("<h2 style='text-align: center; color: black;'>PYTHON - Inteligencia Artificial</h2>", unsafe_allow_html=True)
    
    st.image('https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png')
    
if objetivos:
    st.snow()
    st.image('https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png')
    st.markdown("<h2 style='text-align: color: black;'>Los objetivos de la investigación formativa son:</h2>",unsafe_allow_html=True)

    st.markdown('1. Competencia Comunicativa Presentación de sus resultados con lenguaje de programación Python utilizando los archivos Jupyter Notebook.')


    st.markdown('2. Competencia Aprendizaje: con las aptitudes en Descomposición (desarticular el problema en pequeñas series de soluciones), Reconocimiento de Patrones (encontrar simulitud al momento de resolver problemas), Abstracción (omitir información relevante), Algoritmos (pasos para resolución de un problema)')

    st.markdown('3. Competencia de Trabajo en Equipo: exige habilidades individuales y grupales orientadas a la cooperación, planificación, coordinación, asignación de tareas, cumplimiento de tareas y solución de conflictos en pro de un trabajo colectivo, utilizando los archivos Jupyter Notebook los cuales se sincronizan en el servidor Gitlab con comandos Git.')

    st.image('https://user-images.githubusercontent.com/19308295/115926252-2b8a0c00-a448-11eb-9d9c-b43beaf0ff68.png')

    st.markdown("<h2 style='text-align: center; color: black;'>Aplicación en IA </h2>", unsafe_allow_html=True)

    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
    
if base_teorica:
    st.snow()
    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
    
    st.markdown("<h2 style='text-align: center; color: black;'>Base Teórica</h2>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: color: black;'>Análisis de Correlación</h2>", unsafe_allow_html=True)

    st.markdown('El análisis de correlación es el primer paso para construir modelos explicativos y predictivos más complejos.')

 
    st.markdown('A menudo nos interesa observar y medir la relación entre 2 variables numéricas mediante el análisis de correlación.')

    st.markdown('Se trata de una de las técnicas más habituales en análisis de datos y el primer paso necesario antes de construir cualquier modelo explicativo o predictivo más complejo.')

    st.markdown('Para poder tener el  Datset hay que recolectar información a travez de encuentas.')

    st.markdown("<h2 style='color: black;'>¿Qué es la correlación?</h2>", unsafe_allow_html=True)

    st.markdown('La correlación es un tipo de asociación entre dos variables numéricas, específicamente evalúa la tendencia (creciente o decreciente) en los datos.')

    st.markdown('Dos variables están asociadas cuando una variable nos da información acerca de la otra. Por el contrario, cuando no existe asociación, el aumento o disminución de una variable no nos dice nada sobre el comportamiento de la otra variable.')
 
    st.markdown('Dos variables se correlacionan cuando muestran una tendencia creciente o decreciente.')

    st.markdown("<h2 style='text-align: color: black;'>¿Cómo se mide la correlación?</h2>", unsafe_allow_html=True)

    st.markdown('Tenemos el coeficiente de correlación lineal de Pearson que se sirve para cuantificar tendencias lineales, y el coeficiente de correlación de Spearman que se utiliza para tendencias de aumento o disminución, no necesariamente lineales pero sí monótonas.')

    st.markdown("<h2 style='text-align: color: black;'>Correlación de Pearson</h2>", unsafe_allow_html=True)


    st.markdown('El coeficiente de correlación lineal de Pearson mide una tendencia lineal entre dos variables numéricas.')

    st.markdown('Es el método de correlación más utilizado, pero asume que:.')
    st.markdown('- La tendencia debe ser de tipo lineal.')
    st.markdown('No existen valores atípicos (outliers')
    st.markdown('- Las variables deben ser numéricas.')
    st.markdown('- Tenemos suficientes datos (algunos autores recomiendan tener más de 30 puntos u observaciones).')

    st.markdown('Los dos primeros supuestos se pueden evaluar simplemente con un diagrama de dispersión, mientras que para los últimos basta con mirar los datos y evaluar el diseño que tenemos.')

    st.markdown("<h2 style='text-align: color: black;'>Cómo se interpreta la correlación</h2>", unsafe_allow_html=True)

    st.markdown('El signo nos indica la dirección de la relación, como hemos visto en el diagrama de dispersión.')
    st.markdown('- un valor positivo indica una relación directa o positiva.')
    st.markdown('- un valor negativo indica relación indirecta, inversa o negativa.')
    st.markdown('  - un valor nulo indica que no existe una tendencia entre ambas variables (puede ocurrir que no exista relación o que la relación sea más compleja que una tendencia, por ejemplo, una relación en forma de U).')


    st.markdown('La magnitud nos indica la fuerza de la relación, y toma valores entre $-1$ a $1$. Cuanto más cercano sea el valor a los extremos del intervalo ($1$ o $-1$) más fuerte será la tendencia de las variables, o será menor la dispersión que existe en los puntos alrededor de dicha tendencia. Cuanto más cerca del cero esté el coeficiente de correlación, más débil será la tendencia, es decir, habrá más dispersión en la nube de puntos.')
    st.markdown('- si la correlación vale $1$ o $-1$ diremos que la correlación es “perfecta”.')
    st.markdown('- si la correlación vale $0$ diremos que las variables no están correlacionadas.')

    st.image("https://user-images.githubusercontent.com/25250496/204172549-2ccf3be3-a2b3-4b49-9cd4-adb66e28621d.png")

    st.markdown("<h2 style='text-align: center; color: black;'>Fórmula Coeficiente de Correlación de Pearson</h2>", unsafe_allow_html=True)

    st.image('https://www.questionpro.com/blog/wp-content/uploads/2019/07/analisis-de-correlacion-2.jpg')


    st.markdown('Distancia Euclidiana: La distancia euclidiana es la generalización del teorema de Pitágoras.')

    st.image('http://3.bp.blogspot.com/-YU7iwu9rMIk/TuZLXuWM_8I/AAAAAAAAGNU/DqsQeCkheMk/s1600/Pit%25C3%25A1goras.png')

    st.markdown('Regresión Lineal: La regresión lineal se usa para encontrar una relación lineal entre el objetivo y uno o más predictores.')

    st.image('https://user-images.githubusercontent.com/25250496/204172072-0fabbfdf-1c4c-4f9b-8f42-505d98b18b71.png')

    st.markdown("<h2 style='text-align: color: black;'>Marco teorico</h2>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: color: black;'>¿Que es una gráfica de Dispersión?</h2>", unsafe_allow_html=True)

    st.markdown('La gráfica de dispersión es la visualización de datos que se utiliza cuando hay muchos puntos de datos diferentes y se desea destacar las similitudes en el conjunto de datos. Esto es útil cuando se buscan valores atípicos o para entender la distribución de los datos.')
    st.markdown('Si los datos forman una banda que se extiende desde la parte inferior izquierda a la superior derecha, lo más probable es que exista una correlación positiva entre las dos variables. Si la banda va de la parte superior izquierda a la inferior derecha, es probable que exista una correlación negativa. Si es difícil ver un patrón, es probable que no haya correlación.')


    st.image('https://tudashboard.com/wp-content/uploads/2021/06/Dispersion-1024x862.png')

    st.markdown("<h2 style='text-align: color: black;'>¿Qué es una regresion lineal?</h2>", unsafe_allow_html=True)


    st.markdown('La regresión lineal es una técnica de modelado estadístico que se emplea para describir una variable de respuesta continua como una función de una o varias variables predictoras. Puede ayudar a comprender y predecir el comportamiento de sistemas complejos o a analizar datos experimentales, financieros y biológicos.')

    st.markdown('Las técnicas de regresión lineal permiten crear un modelo lineal. Este modelo describe la relación entre una variable dependiente  y  (también conocida como la respuesta) como una función de una o varias variables independientes  Xi  (denominadas predictores).')

    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Linear_regression.svg/1200px-Linear_regression.svg.png')

    st.markdown("<h2 style='text-align: color: black;'>¿Qué es la correlación de Pearson?</h2>", unsafe_allow_html=True)
            

    st.markdown('Es una prueba que mide la relación estadística entre dos variables continuas. Si la asociación entre los elementos no es lineal, entonces el coeficiente no se encuentra representado adecuadamente.')

    st.markdown('El coeficiente de correlación puede tomar un rango de valores de +1 a -1. Un valor de 0 indica que no hay asociación entre las dos variables. Un valor mayor que 0 indica una asociación positiva. Es decir, a medida que aumenta el valor de una variable, también lo hace el valor de la otra. Un valor menor que 0 indica una asociación negativa; es decir, a medida que aumenta el valor de una variable, el valor de la otra disminuye.')

    st.markdown('Para llevar a cabo la correlación de Pearson es necesario cumplir lo siguiente:')

    st.markdown('- La escala de medida debe ser una escala de intervalo o relación.')
    st.markdown('- Las variables deben estar distribuida de forma aproximada.')
    st.markdown('- La asociación debe ser lineal.')
    st.markdown('- No debe haber valores atípicos en los datos.')

    st.image('https://i.ytimg.com/vi/eTuGHN53kJQ/maxresdefault.jpg')

    st.markdown("<h2 style='text-align: color: black;'>¿Qué es imputacíon en Python?</h2>", unsafe_allow_html=True)

    st.markdown('Hay dos aproximaciones comúnmente usadas para la imputación de los valores perdidos.') 
    st.markdown('La primera técnica consiste en rellenar estos valores con la media (o mediana) de los datos de la variable en el caso de que se trate de una variable numérica. Para el caso de las variables categóricas imputamos los valores perdidos con la moda de la variable.')

    st.image('https://cesarquezadab.com/wp-content/uploads/2021/09/Captura-1.jpg')

    st.markdown("<h2 style='text-align: color: black;'>¿Qué es correlación lineal en Python?</h2>", unsafe_allow_html=True)

    st.markdown('La correlación lineal es un método estadístico que permite cuantificar la relación lineal existente entre dos variables. Existen varios estadísticos, llamados coeficientes de correlación lineal, desarrollados con el objetivo de medir este tipo de asociación, algunos de los más empleados son Pearson, Spearman y Kendall.')

    st.markdown('Con frecuencia, los estudios de correlación lineal preceden a análisis más complejos, como la creación de modelos de regresión. Primero, se analiza si las variables están correlacionadas y, en caso de estarlo, se procede a generar modelos.')
    st.markdown('Es importante destacar que, la existencia de correlación entre dos variables, no implica necesariamente causalidad. La asociación observada puede deberse a un tercer factor (confounder).')

    st.markdown('Correlación lineal con Python.')


    st.markdown('Existen múltiples implementaciones que permiten calcular correlaciones lineales en Python, tres de las más utilizadas están disponibles en las librerías: SciPy, Pandas y Pingouin.')

    st.image('https://i.ytimg.com/vi/UUQMstPRfFM/sddefault.jpg')

    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
    
    
if propuesta:
    st.snow()
    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
    st.markdown("<h2 style='text-align: center; color: black;'>Propuesta</h2>", unsafe_allow_html=True)

    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')

    st.markdown("<h2 style='color: black;'>1.- Dataset</h2>", unsafe_allow_html=True)

    st.markdown("<h2 style='color: black;'>Formulario de Google </h2>", unsafe_allow_html=True)

    st.markdown("<h2 style='color: black;'>Preguntas </h2>", unsafe_allow_html=True)

    st.markdown('Del uno al cinco segun la escala dada califique las siguientes comidas:')

    st.markdown('1. Me desagrada')
    st.markdown('2. No me gusta')
    st.markdown('3. Es aceptable')
    st.markdown('4. Agradable')
    st.markdown('5. Me encantan')

    st.markdown('Formulario de Google') 

    st.markdown('Preparacion y pregunta de pasos para realizar la encuesta.')

    st.image('https://cdn.discordapp.com/attachments/952764370335719434/1049148181646163998/image.png')
    st.image('https://cdn.discordapp.com/attachments/952764370335719434/1049538764353060944/1.png')
    st.image('https://cdn.discordapp.com/attachments/952764370335719434/1049538764353060944/1.png')

    st.markdown("<h2 style='color: black;'>PFormulario de Google (Preprocesamiento) </h2>", unsafe_allow_html=True)

    st.markdown('Procedemos a crear nuestro exel para luego ser convertido en un archivo csv con el fin de utilizarlo junto al comando panda y numpy.')

    st.image('https://cdn.discordapp.com/attachments/952764370335719434/1049149904171319357/861555e9-e206-4d22-a2c5-d4d370966a98.png')
    st.image('https://cdn.discordapp.com/attachments/952764370335719434/1049542478019178546/ZHiqJFM83PseYpWGGozUQAfiovfpVIiwF3y-v6CFKFIMxSP0y7VzelQL1DPFCdlw_bc-HwihIXwQ5l0ksErhLDgJBGCWuVUp4Z5pcon_3sjRYxxRBiXmAoD3mAgWC6c4VvA0xCgM3ul6QEVk_VUDwqxh6pT78X-HPjsKBjBxfQgpzuyTfCAnXFY1kf7OCLN0r43zdJVLMZaeQC2Sxp9Si9y8adGgduBPdX3vegeVk28yS8oP7U4cBFeamc_PYwGK7VmzK0sUexfN9WRr1DIT7oAGeKxzrSE4SslSVRIF-TGD-hkNb8D7CnOQN-UzERY9B2gBNbFo6fswgFRRTesnCc-yfZYTDhjldNwPshHPTSiapc18_zRfyEICfJ8TRrGd4nLPD5yHp0X6yBrZ6XkhUjWjGyHvs4x0k0QEUdSNpSiPnOMxG54Vgxl7ZgS-BvZoq3sQ9vnrJsOqAi6_eYRkAjRpI7h2Fk55zRPNPGZCeooLJWKLXOabBkVyL00q..png')
    st.image('https://cdn.discordapp.com/attachments/952764370335719434/1049542753215844362/wQUeVtzifEvpulCDOfjZzswrSFUFQArGVR50Udx4d1iVPKhcpQXOnH3CnZTMD-98RY7SeX9BlgdrhTIjnyUEX8eXHkaNHfY9JsC-h5J_icllATWlQUcg37rk1vjsmwRfD0DlpS4IFhbVQ8Y0ooJKFx8uxZknzhd7A0lmGHKStS25ekzRv3YR8daV97wxlvDrwVDOmADCJKjWN9Yp4cmzLouLjMX96fdXy4ZqRRN8Mz9or5FXJYf6_PZjz_0zfPwc0qwuzfmQGmqYvvoJtevGEKGyJMqU0XAH0p51vciQ0md5mGcXcIYsy_IQ0zu0_--dpXVASyNZ2T769qnHUzfY204EFObq0FhNO1sZMuvs9bw4sD2Pnyip3CgdZDkGIbvEl0XQtovzxR9CiGG-wFX65jR6iA0YX4g5_viKdjF2gklfnnKSMGZ5FzRp4fLilYtR_6rYDRSxtvnoZ7bIHxX2IGKKGGIdd9Iw_v2fVX64mXzLMcXPS6v62kv5wwW2..png')
    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
    st.markdown("<h2 style='text-align: center; color: black;'>Archivo CSV separado por comas</h2>", unsafe_allow_html=True)
    pandas = pd.read_csv('formulario 1.csv')
    st.dataframe(pandas)
    st.markdown('Cantidad de Filas y Columnas')
    
    st.markdown('46 Columnas y 33 Filas')
    
    
if correlacion_de_pearson:
    st.snow()
    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
    st.markdown("<h2 style='text-align: center; color: black;'>Correlacion de Pearson y Sustitucion de valores NAN</h2>", unsafe_allow_html=True)
    pandas = pd.read_csv('formulario 1.csv')
    st.markdown('Se visualiza los valores NAN que seran imputados en el dataframe')
    st.dataframe(pandas)
    st.markdown('Se muestra donde se encuentran los valores NAN (float64)')
    pandas.dtypes
    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
    st.markdown("<h2 style='text-align: center; color: black;'>Tabla limpia de valores NAN</h2>", unsafe_allow_html=True)
    st.markdown('Los valores que reemplazaron los NAN son la media')
    pandas['Pachamanca'] = pandas['Pachamanca'].replace(np.nan, 4)
    pandas['Escabeche de pollo'] = pandas['Escabeche de pollo'].replace(np.nan, 3)
    pandas['Chupe de camarón'] = pandas['Chupe de camarón'].replace(np.nan, 4)
    pandas['Pollo a la brasa'] = pandas['Pollo a la brasa'].replace(np.nan, 4)
    pandas['cecina'] = pandas['cecina'].replace(np.nan, 3)
    pandas['Sushi'] = pandas['Sushi'].replace(np.nan, 3)
    pandas['Tacos'] = pandas['Tacos'].replace(np.nan, 3)
    pandas['Carapulcra'] = pandas['Carapulcra'].replace(np.nan, 3)
    pandas["Tallarines"] = pandas["Tallarines"].replace(np.nan, 4)
    pandas['Anticuchos'] = pandas['Anticuchos'].replace(np.nan, 4)
    pandas['Locro de zapallo'] = pandas['Locro de zapallo'].replace(np.nan, 4)
    pandas['Bistec a lo pobre'] = pandas['Bistec a lo pobre'].replace(np.nan, 4)
    pandas['Choritos a la chalaca'] = pandas['Choritos a la chalaca'].replace(np.nan, 3)
    st.dataframe(pandas)
    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
    st.markdown("<h2 style='text-align: center; color: black;'>Tabla de Correlacion de Pandas</h2>", unsafe_allow_html=True)
    n = pandas[pandas.columns[1:]].to_numpy()
    m = pandas[pandas.columns[0]].to_numpy()
    dataframe_pandas = pd.DataFrame(n.T, columns = m)
    matrix_correlacion = dataframe_pandas.corr()
    matrix_correlacion
    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
    
    
if nuestra_correlacion:
    st.snow()
    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
    pandas = pd.read_csv('formulario 1.csv')
    st.markdown("<h2 style='text-align: center; color: black;'>Nuestro Algoritmo y su Respectivo Grafico</h2>", unsafe_allow_html=True)
    st.markdown('Para esta parte hemos tomado la el dataframe limpio de valores NAN, para poder realizar nuestro algoritmo de correlacion, empezamos eliminando la columna de correo electronico para solo tener una dataframe de valores numericos. ')
    pandas['Pachamanca'] = pandas['Pachamanca'].replace(np.nan, 4)
    pandas['Escabeche de pollo'] = pandas['Escabeche de pollo'].replace(np.nan, 3)
    pandas['Chupe de camarón'] = pandas['Chupe de camarón'].replace(np.nan, 4)
    pandas['Pollo a la brasa'] = pandas['Pollo a la brasa'].replace(np.nan, 4)
    pandas['cecina'] = pandas['cecina'].replace(np.nan, 3)
    pandas['Sushi'] = pandas['Sushi'].replace(np.nan, 3)
    pandas['Tacos'] = pandas['Tacos'].replace(np.nan, 3)
    pandas['Carapulcra'] = pandas['Carapulcra'].replace(np.nan, 3)
    pandas["Tallarines"] = pandas["Tallarines"].replace(np.nan, 4)
    pandas['Anticuchos'] = pandas['Anticuchos'].replace(np.nan, 4)
    pandas['Locro de zapallo'] = pandas['Locro de zapallo'].replace(np.nan, 4)
    pandas['Bistec a lo pobre'] = pandas['Bistec a lo pobre'].replace(np.nan, 4)
    pandas['Choritos a la chalaca'] = pandas['Choritos a la chalaca'].replace(np.nan, 3) 
    n = pandas[pandas.columns[1:]].to_numpy()
    m = pandas[pandas.columns[0]].to_numpy()
    dataframe_pandas = pd.DataFrame(n.T, columns = m)
    matrix_correlacion = dataframe_pandas.corr()
    
    with st.echo():       
        dataframe1 = pd.DataFrame(pandas)
        #convertir en una lista la primera columna
        lista1 = dataframe1['Dirección de correo electrónico'].tolist()
        A = n
        B = n
        # Creando una lista para almacenar los resultados 
        coeficientes_pearson = []
        # Calcular la correlacion de pearson
        for i in range(len(A)):
            for j in range(len(B)):        
                # Calcular la media de la columna A
                media_A = sum(A[i])/len(A[i])        
                # Calcular la media de la columna B
                media_B = sum(B[j])/len(B[j])        
                # Calcular el numerador
                numerador = 0
                for k in range(len(A[i])):
                    numerador += (A[i][k] - media_A)*(B[j][k] - media_B)            
                # Calcular el denominador
                denominador_A = 0
                denominador_B = 0
                for k in range(len(A[i])):
                    denominador_A += (A[i][k] - media_A)**2
                    denominador_B += (B[j][k] - media_B)**2
                denominador = (denominador_A * denominador_B)**0.5
                # Calcular el coeficiente de pearson
                r = numerador/denominador
                coeficientes_pearson.append(r)
        # Crear matriz de correlacion de pearson
        matriz_correlacion_pearson = []
        for i in range(len(A)):
            matriz_correlacion_pearson.append(coeficientes_pearson[i*len(B):(i+1)*len(B)])
        # Crear el dataframe
        dataframe_correlacion_pearson = pd.DataFrame(matriz_correlacion_pearson, 
                                                     columns=lista1, 
                                                     index=lista1)
    st.dataframe(dataframe_correlacion_pearson)
    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
    st.markdown("<h2 style='text-align: center; color: black;'>Mayor Valor de Correlacion</h2>", unsafe_allow_html=True)
    pandas = pd.read_csv('formulario 1.csv')
    pandas['Pachamanca'] = pandas['Pachamanca'].replace(np.nan, 4)
    pandas['Escabeche de pollo'] = pandas['Escabeche de pollo'].replace(np.nan, 3)
    pandas['Chupe de camarón'] = pandas['Chupe de camarón'].replace(np.nan, 4)
    pandas['Pollo a la brasa'] = pandas['Pollo a la brasa'].replace(np.nan, 4)
    pandas['cecina'] = pandas['cecina'].replace(np.nan, 3)
    pandas['Sushi'] = pandas['Sushi'].replace(np.nan, 3)
    pandas['Tacos'] = pandas['Tacos'].replace(np.nan, 3)
    pandas['Carapulcra'] = pandas['Carapulcra'].replace(np.nan, 3)
    pandas["Tallarines"] = pandas["Tallarines"].replace(np.nan, 4)
    pandas['Anticuchos'] = pandas['Anticuchos'].replace(np.nan, 4)
    pandas['Locro de zapallo'] = pandas['Locro de zapallo'].replace(np.nan, 4)
    pandas['Bistec a lo pobre'] = pandas['Bistec a lo pobre'].replace(np.nan, 4)
    pandas['Choritos a la chalaca'] = pandas['Choritos a la chalaca'].replace(np.nan, 3)    
    n = pandas[pandas.columns[1:]].to_numpy()
    m = pandas[pandas.columns[0]].to_numpy()
    dataframe_pandas = pd.DataFrame(n.T, columns = m)
    matrix_correlacion = dataframe_pandas.corr()
    matrix_correlacion_pandas = np.round(matrix_correlacion, decimals = 4)
    with st.echo():   
        #remplazamos el valor 1 por 0
        matrix_correlacion_pandas[matrix_correlacion_pandas == 1]=0
        #hallamos y guardamos los maximos de cada columna en la matriz primero
        primero = matrix_correlacion_pandas.max()
        #comparamos todos los mayores para sacar el mayor de todos y ordenamos de mayor a menor
        ordenado = primero.sort_values(ascending =
                         False)
    st.write(ordenado)   
    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
    
if mapa_de_calor:
    st.snow()
    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
    pandas = pd.read_csv('formulario 1.csv')
    dataframe1 = pd.DataFrame(pandas)
    lista1 = dataframe1['Dirección de correo electrónico'].tolist()
    pandas['Pachamanca'] = pandas['Pachamanca'].replace(np.nan, 4)
    pandas['Escabeche de pollo'] = pandas['Escabeche de pollo'].replace(np.nan, 3)
    pandas['Chupe de camarón'] = pandas['Chupe de camarón'].replace(np.nan, 4)
    pandas['Pollo a la brasa'] = pandas['Pollo a la brasa'].replace(np.nan, 4)
    pandas['cecina'] = pandas['cecina'].replace(np.nan, 3)
    pandas['Sushi'] = pandas['Sushi'].replace(np.nan, 3)
    pandas['Tacos'] = pandas['Tacos'].replace(np.nan, 3)
    pandas['Carapulcra'] = pandas['Carapulcra'].replace(np.nan, 3)
    pandas["Tallarines"] = pandas["Tallarines"].replace(np.nan, 4)
    pandas['Anticuchos'] = pandas['Anticuchos'].replace(np.nan, 4)
    pandas['Locro de zapallo'] = pandas['Locro de zapallo'].replace(np.nan, 4)
    pandas['Bistec a lo pobre'] = pandas['Bistec a lo pobre'].replace(np.nan, 4)
    pandas['Choritos a la chalaca'] = pandas['Choritos a la chalaca'].replace(np.nan, 3)    
    n = pandas[pandas.columns[1:]].to_numpy()
    m = pandas[pandas.columns[0]].to_numpy()
    dataframe_pandas = pd.DataFrame(n.T, columns = m)
    matrix_correlacion = dataframe_pandas.corr()
    matrix_correlacion_pandas = np.round(matrix_correlacion, decimals = 4)  

    #convertir en una lista la primera columna
    lista1 = dataframe1['Dirección de correo electrónico'].tolist()
    A = n
    B = n
    # Creando una lista para almacenar los resultados 
    coeficientes_pearson = []
    # Calcular la correlacion de pearson
    for i in range(len(A)):
        for j in range(len(B)):        
            # Calcular la media de la columna A
            media_A = sum(A[i])/len(A[i])        
            # Calcular la media de la columna B
            media_B = sum(B[j])/len(B[j])        
            # Calcular el numerador
            numerador = 0
            for k in range(len(A[i])):
                numerador += (A[i][k] - media_A)*(B[j][k] - media_B)            
            # Calcular el denominador
            denominador_A = 0
            denominador_B = 0
            for k in range(len(A[i])):
                denominador_A += (A[i][k] - media_A)**2
                denominador_B += (B[j][k] - media_B)**2
            denominador = (denominador_A * denominador_B)**0.5        
            # Calcular el coeficiente de pearson
            r = numerador/denominador
            coeficientes_pearson.append(r)
    # Crear matriz de correlacion de pearson
    matriz_correlacion_pearson = []
    for i in range(len(A)):
        matriz_correlacion_pearson.append(coeficientes_pearson[i*len(B):(i+1)*len(B)])
    # Crear el dataframe
    dataframe_correlacion_pearson = pd.DataFrame(matriz_correlacion_pearson, 
                                                 columns=lista1, 
                                                 index=lista1)   
    st.markdown("<h2 style='text-align: center; color: black;'>Mapa de Calor</h2>", unsafe_allow_html=True)
    st.markdown('En esta seccion se mostraran los mapas de calor obtenidos mediante la libreria pandas y el obtenido desde nuestro algoritmo. Comparando ambas para poder confirmar su similitud.')
    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
    st.markdown("<h2 style='text-align:; color: black;'>Mapa de Calor de Pandas</h2>", unsafe_allow_html=True)
    st.image('https://scontent.faqp2-3.fna.fbcdn.net/v/t39.30808-6/320568454_821952312437453_6275346164755308970_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeHSHS3jnyf3Mjzbox56D96_7xz6F8BIZ6nvHPoXwEhnqd3dfIxG5PHyw7pkK4KTSEtKqPkC1bKrWiT6mmRfX4Hx&_nc_ohc=-nHPUXn5WA4AX8oiYSw&_nc_ht=scontent.faqp2-3.fna&oh=00_AfCXoxyC5ZZTnmNz80jKbb1lfQJF-tdqQsMDfBUy7HLuuQ&oe=63A59FA7')
    st.markdown("<h2 style='text-align:; color: black;'>Mapa de Calor de Nuestro Algoritmo </h2>", unsafe_allow_html=True)
    st.image('https://scontent.faqp2-3.fna.fbcdn.net/v/t39.30808-6/320568454_821952312437453_6275346164755308970_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeHSHS3jnyf3Mjzbox56D96_7xz6F8BIZ6nvHPoXwEhnqd3dfIxG5PHyw7pkK4KTSEtKqPkC1bKrWiT6mmRfX4Hx&_nc_ohc=-nHPUXn5WA4AX8oiYSw&_nc_ht=scontent.faqp2-3.fna&oh=00_AfCXoxyC5ZZTnmNz80jKbb1lfQJF-tdqQsMDfBUy7HLuuQ&oe=63A59FA7')
    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')


if validacion_de_resultados:
    st.snow()
    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
    st.markdown("<h2 style='text-align: center; color: black;'>Validacion de Resultados</h2>", unsafe_allow_html=True)
    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
    st.markdown("<h2 style='text-align: ; color: black;'>Validacion-Matrix de Correlacion</h2>", unsafe_allow_html=True)
    st.markdown('Se debe llenar la tabla de VALIDACIÓN de la Matriz de Correlación con los valores de Similitud obtenidos En `NUMPY` a partir de las matrices n y m con funciones. Se realiza la validación de los resultados obtenidos con la Matriz de Correlación de Pearson en Numpy.')
    st.markdown("<h2 style='text-align: ; color: black;'>Validacion de Resultados de Pandas</h2>", unsafe_allow_html=True)
    st.markdown('Valores de Similitud en pandas')
    pandas = pd.read_csv('formulario 1.csv')
    dataframe1 = pd.DataFrame(pandas)
    lista1 = dataframe1['Dirección de correo electrónico'].tolist()
    pandas['Pachamanca'] = pandas['Pachamanca'].replace(np.nan, 4)
    pandas['Escabeche de pollo'] = pandas['Escabeche de pollo'].replace(np.nan, 3)
    pandas['Chupe de camarón'] = pandas['Chupe de camarón'].replace(np.nan, 4)
    pandas['Pollo a la brasa'] = pandas['Pollo a la brasa'].replace(np.nan, 4)
    pandas['cecina'] = pandas['cecina'].replace(np.nan, 3)
    pandas['Sushi'] = pandas['Sushi'].replace(np.nan, 3)
    pandas['Tacos'] = pandas['Tacos'].replace(np.nan, 3)
    pandas['Carapulcra'] = pandas['Carapulcra'].replace(np.nan, 3)
    pandas["Tallarines"] = pandas["Tallarines"].replace(np.nan, 4)
    pandas['Anticuchos'] = pandas['Anticuchos'].replace(np.nan, 4)
    pandas['Locro de zapallo'] = pandas['Locro de zapallo'].replace(np.nan, 4)
    pandas['Bistec a lo pobre'] = pandas['Bistec a lo pobre'].replace(np.nan, 4)
    pandas['Choritos a la chalaca'] = pandas['Choritos a la chalaca'].replace(np.nan, 3)    
    n = pandas[pandas.columns[1:]].to_numpy()
    m = pandas[pandas.columns[0]].to_numpy()
    dataframe_pandas = pd.DataFrame(n.T, columns = m)
    matrix_correlacion = dataframe_pandas.corr()
    matrix_correlacion_pandas = np.round(matrix_correlacion, decimals = 4)
    with st.echo():
        #remplazamos el valor 1 por 0
        matrix_correlacion_pandas[matrix_correlacion_pandas == 1]=0
        #hallamos y guardamos los maximos de cada columna en la matriz primero
        primero = matrix_correlacion_pandas.max()
        #comparamos todos los mayores para sacar el mayor de todos
    st.write('1. alejanira17@gmail.com  y dttitopalominoevelynadriana12@gmail.com  obtienen el **PRIMER** indice mas alto de similitud con',primero.max())

    with st.echo():
        #usamos todos los mayores para remplazar el primer mayor anterior por cero
        primero[primero == 0.7834]= 0
        #comparamos todos los mayores para hallar el segundo amyor
    st.write('2. ttitopalominoevelynadriana12@gmail.com y jensenruiznolasco@gmail.com obtienen el **SEGUNDO** indice mas alto de similitud con',primero.max())
    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
    st.markdown("<h2 style='text-align: ; color: black;'>Los Resultados Correspondientes son:</h2>", unsafe_allow_html=True)
    st.markdown('alejanira17@gmail.com  y dttitopalominoevelynadriana12@gmail.com  obtienen el **PRIMER** indice mas alto de similitud con 0.7834')
    st.markdown('ttitopalominoevelynadriana12@gmail.com y jensenruiznolasco@gmail.com obtienen el **SEGUNDO** indice mas alto de similitud con 0.7336')
    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
    
    st.markdown("<h2 style='text-align: ; color: black;'>Validacion de Nuestros Resultados</h2>", unsafe_allow_html=True)
    
    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
    
    with st.echo():
        # Paso 1: tomar dos listas de valores
        lista_a = n[4]
        lista_b = n[40]
        # PRIMERA PARTE    
        # Paso 2: calcular la media de cada lista
        media_a = sum(lista_a) / len(lista_a)
        media_b = sum(lista_b) / len(lista_b)    
        # Paso 3: calcular la diferencia entre cada elemento de la lista y la media
        diferencia_a = [x - media_a for x in lista_a]
        diferencia_b = [x - media_b for x in lista_b]    
        # Paso 4: multiplicar cada diferencia de la lista entre sí
        multiplicacion = [x * y for x, y in zip(diferencia_a, diferencia_b)]    
        # Paso 5: calcular la suma de todas las multiplicaciones
        #suma_multiplicacion
        suma_multiplicacion = sum(multiplicacion)    
        # SEGUNDA PARTE     
        # Paso 6: calcular los cuadrados de la suma de cada lista
        cuadrados_a = sum([x**2 for x in diferencia_a])
        cuadrados_b = sum([x**2 for x in diferencia_b])        
        #TERCERA PARTE APLICACION DE LA FORMULA    
        # Paso 7: calcular el coeficiente de correlación de Pearson    
        coef_correlacion_pearson = suma_multiplicacion / (cuadrados_a * cuadrados_b)**0.5    
    st.write('lejanira17@gmail.com  y dttitopalominoevelynadriana12@gmail.com  obtienen el **PRIMER** indice mas alto de similitud con',coef_correlacion_pearson)
    with st.echo():
        #Paso 1: tomar dos listas de valores
        lista_a = n[40]
        lista_b = n[35]
        # PRIMERA PARTE   
        # Paso 2: calcular la media de cada lista
        media_a = sum(lista_a) / len(lista_a)
        media_b = sum(lista_b) / len(lista_b)       
        # Paso 3: calcular la diferencia entre cada elemento de la lista y la media
        diferencia_a = [x - media_a for x in lista_a]
        diferencia_b = [x - media_b for x in lista_b]        
        # Paso 4: multiplicar cada diferencia de la lista entre sí
        multiplicacion = [x * y for x, y in zip(diferencia_a, diferencia_b)]        
        # Paso 5: calcular la suma de todas las multiplicaciones
        #suma_multiplicacion
        suma_multiplicacion = sum(multiplicacion)        
        # SEGUNDA PARTE         
        # Paso 6: calcular los cuadrados de la suma de cada lista
        cuadrados_a = sum([x**2 for x in diferencia_a])
        cuadrados_b = sum([x**2 for x in diferencia_b])              
        #TERCERA PARTE APLICACION DE LA FORMULA        
        # Paso 7: calcular el coeficiente de correlación de Pearson        
        coef_correlacion_pearson = suma_multiplicacion / (cuadrados_a * cuadrados_b)**0.5                
    st.write('ttitopalominoevelynadriana12@gmail.com y jensenruiznolasco@gmail.com obtienen el **SEGUNDO** indice mas alto de similitud con',coef_correlacion_pearson)
    st.markdown("<h2 style='text-align: ; color: black;'>Nuestros Resultados son:</h2>", unsafe_allow_html=True)
    st.markdown('alejanira17@gmail.com  y dttitopalominoevelynadriana12@gmail.com  obtienen el **PRIMER** indice mas alto de similitud con 0.7834')
    st.markdown('ttitopalominoevelynadriana12@gmail.com y jensenruiznolasco@gmail.com obtienen el **SEGUNDO** indice mas alto de similitud con 0.7336')
    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
      
    
if conclusiones:
    st.snow()

    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')  
    st.markdown("<h2 style='text-align: center ; color: black;'>Conclusiones</h2>", unsafe_allow_html=True)
    
    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
    st.markdown("<h2 style='text-align: ; color: black;'>¿Se valido o no los resultados?</h2>", unsafe_allow_html=True)
    st.markdown('Los datos fueron obtenidos desde una encuesta confiable, realizada mediante un formulario de google, para despues ser convertido en un archivo CSV y utilizarlo conjuntamente con las librerias de data science Pandas, Seaborn, Matplotlib y Numpy. De los cuales nos proporcionaron relaciones existentes entre los datos de gran similitud, maximos, minimos,etc.')
    
    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
    st.markdown("<h2 style='text-align: ; color: black;'>¿Es efectivo el metodo de correlación de pearson?</h2>", unsafe_allow_html=True)
    st.markdown('La correlacion de pearson fue una gran herramienta para calcular la correlacion existente entre datos en los cuadros de doble entrada, estos valores necesitan ser de manera cuantitativa expresado en valores nuemricos. Por los tanto podemos decir que el metodo de correlacion de Pearson si es efectivo, dado que sirve y es de gran utilidad para hallar correlacion entre datos siendo de gran utilidad en el area cientifica, desde estudios técnicos, econométricos o de inge- niería; hasta investigaciones relacionadas con las ciencias sociales, del comportamiento o de la salud.')
    
    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
    st.markdown("<h2 style='text-align: ; color: black;'>Los resultados Validados son:</h2>", unsafe_allow_html=True)
    st.markdown('Segun los resultados que fueron validos con Pandas y nuestro algoritmo los datos validados seria')
    st.markdown('1. El indice mas alto de similitud, lejanira17@gmail.com y dttitopalominoevelynadriana12@gmail.com obtienen el PRIMER indice mas alto de similitud con 0.783417488637325')
    st.markdown('2. El segundo indice mas alto de similitud ttitopalominoevelynadriana12@gmail.com y jensenruiznolasco@gmail.com obtienen el SEGUNDO indice mas alto de similitud con 0.7336')
    st.markdown('3. La grafica de calor')
    st.image('https://scontent.faqp2-3.fna.fbcdn.net/v/t39.30808-6/320568454_821952312437453_6275346164755308970_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeHSHS3jnyf3Mjzbox56D96_7xz6F8BIZ6nvHPoXwEhnqd3dfIxG5PHyw7pkK4KTSEtKqPkC1bKrWiT6mmRfX4Hx&_nc_ohc=-nHPUXn5WA4AX8oiYSw&_nc_ht=scontent.faqp2-3.fna&oh=00_AfCXoxyC5ZZTnmNz80jKbb1lfQJF-tdqQsMDfBUy7HLuuQ&oe=63A59FA7')
    
    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
    st.markdown("<h2 style='text-align: ; color: black;'>Correlación de Pearson y Regresión Lineal, ¿cual es su relación?</h2>", unsafe_allow_html=True)
    st.markdown('En este caso el coeficiente de correlación de Pearson, es el que mide la regresion lineal de los datos obtenidos, por lo tanto la regresion lineal es parte de la correlacion de pearson tomando. Siendo la correlacion de pearson el metodo y la regresion lineal el resultado.')
    
    
    st.image('https://user-images.githubusercontent.com/19308295/115926262-2fb62980-a448-11eb-8189-c2f10e499944.png')
    
    
       
