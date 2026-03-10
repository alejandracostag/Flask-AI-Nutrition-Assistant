import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from groq import Groq
import markdown

load_dotenv()

app = Flask(__name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

niveles_actividad = [
    ('sedentario', 'Sedentario (Poco o ningún ejercicio)'),
    ('poco_activo', 'Poco Activo (1-3 días/semana)'),
    ('moderadamente_activo', 'Moderadamente Activo (3-5 días/semana)'),
    ('muy_activo', 'Muy Activo (6-7 días/semana)'),
    ('super_activo', 'Super Activo (Atleta profesional/2x entrenamientos)')
]

@app.route("/", methods=["GET", "POST"])
def index():
    respuesta = ""

    if request.method == "POST":
        edad = request.form.get("edad")
        nivel_actividad = request.form.get("nivel_actividad")
        comidas_favoritas = request.form.get("comidas_favoritas")
        restricciones = request.form.get("restricciones")

        if not restricciones:
            restricciones = "Ninguna"

        prompt = f"""
Como nutricionista profesional, crea un plan de nutrición personalizado para alguien con el siguiente perfil:

Edad: {edad} años
Nivel de Actividad: {nivel_actividad}
Comidas Favoritas: {comidas_favoritas}
Restricciones Dietéticas/Alergias: {restricciones}

Por favor, proporciona:
1. Estimación de necesidades calóricas diarias
2. Distribución recomendada de macronutrientes
3. Un plan de comidas diario de ejemplo incorporando sus comidas favoritas cuando sea posible
4. Consideraciones nutricionales específicas para su grupo de edad
5. Recomendaciones basadas en su nivel de actividad
6. Alternativas seguras para cualquier alimento restringido
7. 2-3 sugerencias de snacks saludables

Formatea la respuesta claramente con encabezados y puntos para facilitar la lectura.
Ten en cuenta la salud y la seguridad, especialmente con respecto a las restricciones mencionadas.
"""

        try:
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "Eres un nutricionista profesional que da recomendaciones claras, seguras y bien estructuradas."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=900
            )

            respuesta = markdown.markdown(completion.choices[0].message.content)

        except Exception as e:
            respuesta = f"Error al generar el plan nutricional: {str(e)}"

    return render_template(
        "index.html",
        niveles_actividad=niveles_actividad,
        respuesta=respuesta
    )

if __name__ == "__main__":
    app.run(debug=True)