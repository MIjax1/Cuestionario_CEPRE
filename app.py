import streamlit as st
import random
import datetime

# Configure Page Settings
st.set_page_config(
    page_title="Examen para Cinthia Paye",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Modern, Sleek Visual Presentation & High-Contrast Table Display
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    /* Header Container */
    .main-header {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #d946ef 100%);
        padding: 2.2rem;
        border-radius: 24px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 12px 30px -10px rgba(124, 58, 237, 0.45);
    }
    
    .main-header h1 {
        font-size: 2.4rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.5px;
        color: #ffffff !important;
    }
    
    .main-header p {
        font-size: 1.05rem;
        opacity: 0.95;
        margin-top: 0.6rem;
        margin-bottom: 0;
    }

    .badge-container {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-top: 1.2rem;
        flex-wrap: wrap;
    }

    .badge {
        background: rgba(255, 255, 255, 0.22);
        backdrop-filter: blur(12px);
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        border: 1px solid rgba(255, 255, 255, 0.35);
        color: white;
    }

    /* Category Pill */
    .category-pill {
        display: inline-block;
        background: #e0e7ff;
        color: #4338ca;
        padding: 4px 14px;
        border-radius: 12px;
        font-size: 0.78rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.8rem;
    }

    /* Score Cards */
    .score-card-excelente {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        padding: 2.2rem;
        border-radius: 24px;
        text-align: center;
        box-shadow: 0 12px 30px -8px rgba(16, 185, 129, 0.4);
        margin-bottom: 2rem;
    }

    .score-card-bueno {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        padding: 2.2rem;
        border-radius: 24px;
        text-align: center;
        box-shadow: 0 12px 30px -8px rgba(59, 130, 246, 0.4);
        margin-bottom: 2rem;
    }

    .score-card-regular {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: white;
        padding: 2.2rem;
        border-radius: 24px;
        text-align: center;
        box-shadow: 0 12px 30px -8px rgba(245, 158, 11, 0.4);
        margin-bottom: 2rem;
    }

    .score-number {
        font-size: 4.5rem;
        font-weight: 800;
        line-height: 1;
        margin: 0.8rem 0;
        letter-spacing: -2px;
    }

    /* Question Header */
    .q-title {
        color: #4f46e5;
        font-size: 0.9rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.3rem;
    }

    .q-text {
        font-size: 1.22rem;
        font-weight: 600;
        line-height: 1.5;
        color: #1f2937;
        margin-bottom: 1.2rem;
    }

    /* Metric pill */
    .metric-pill {
        background: #f8fafc;
        border-radius: 16px;
        padding: 14px 20px;
        text-align: center;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    
    .metric-val {
        font-size: 1.6rem;
        font-weight: 700;
    }

    .metric-lbl {
        font-size: 0.8rem;
        color: #64748b;
        text-transform: uppercase;
        font-weight: 600;
        margin-top: 2px;
    }

    /* Creative Resolution Box */
    .resolution-box {
        background: #f0fdf4;
        border-left: 5px solid #22c55e;
        padding: 1.2rem 1.4rem;
        border-radius: 12px;
        margin-top: 1rem;
    }

    .resolution-box-wrong {
        background: #fef2f2;
        border-left: 5px solid #ef4444;
        padding: 1.2rem 1.4rem;
        border-radius: 12px;
        margin-top: 1rem;
    }

    .step-box {
        background: #ffffff !important;
        border: 1px solid #cbd5e1;
        border-radius: 10px;
        padding: 0.8rem 1rem;
        margin-top: 0.6rem;
        font-size: 0.92rem;
        color: #0f172a !important;
    }

    /* High Contrast Table Styling for Light and Dark Modes */
    .visual-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        margin-top: 0.8rem;
        font-size: 0.92rem;
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #cbd5e1;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }

    .visual-table th {
        background: #4f46e5 !important;
        color: #ffffff !important;
        padding: 10px 14px;
        text-align: center;
        font-weight: 700;
        border-bottom: 2px solid #3730a3;
    }

    .visual-table td {
        padding: 10px 14px;
        border-bottom: 1px solid #e2e8f0;
        text-align: center;
        background: #ffffff !important;
        color: #0f172a !important;
        font-weight: 500;
    }

    .visual-table tr:last-child td {
        border-bottom: none;
    }

    .highlight-row td {
        background: #fef08a !important;
        color: #854d0e !important;
        font-weight: 700 !important;
    }

    /* Primary buttons custom style */
    div.stButton > button {
        border-radius: 12px;
        font-weight: 600;
        padding: 0.5rem 1.5rem;
        transition: all 0.2s ease;
    }
</style>
""", unsafe_allow_html=True)

# Master Question Pool Definition with Visual & Creative Explanations
BASE_QUESTIONS = [
    {
        "id": 1,
        "category": "⭕ Ordenamiento Circular",
        "question": "Cuatro amigas (Ana, Betty, Carla y Diana) se sientan alrededor de una mesa circular con 4 sillas distribuidas simétricamente. Se sabe que: Ana se sienta frente a la que estudia Derecho; Betty está a la derecha de la que estudia Medicina; Carla no estudia Derecho ni Medicina; Diana está frente a la que estudia Arquitectura; La que estudia Contabilidad está sentada frente a Betty. ¿Quién estudia Contabilidad y qué estudia Carla?",
        "options": [
            ("A", "A) Betty – Derecho"),
            ("B", "B) Ana – Arquitectura"),
            ("C", "C) Ana – Contabilidad"),
            ("D", "D) Diana – Medicina"),
            ("E", "E) Betty – Arquitectura")
        ],
        "correct": "B",
        "steps": [
            "1️⃣ **Frente a Betty:** La que estudia Contabilidad se sienta frente a Betty => Betty NO estudia Contabilidad.",
            "2️⃣ **Ubicación de Betty:** Betty está a la derecha de la de Medicina => Diana estudia Medicina (al Oeste) y Betty está al Norte.",
            "3️⃣ **Frente a Diana:** Carla está frente a Diana (al Este) y estudia Arquitectura.",
            "4️⃣ **Estudiante de Contabilidad:** Ana se sienta al Sur (frente a Betty) y estudia Contabilidad. Betty estudia Derecho."
        ],
        "visual_html": """
        <table class="visual-table">
            <thead>
                <tr><th>Posición</th><th>Amiga</th><th>Carrera Profesional</th></tr>
            </thead>
            <tbody>
                <tr><td><b>Norte</b></td><td>Betty</td><td>Derecho</td></tr>
                <tr class="highlight-row"><td><b>Sur</b></td><td>Ana (Respuesta)</td><td>Contabilidad (Frente a Betty)</td></tr>
                <tr class="highlight-row"><td><b>Este</b></td><td>Carla (Respuesta)</td><td>Arquitectura (Frente a Diana)</td></tr>
                <tr><td><b>Oeste</b></td><td>Diana</td><td>Medicina</td></tr>
            </tbody>
        </table>
        """,
        "summary": "La persona que estudia Contabilidad es **Ana** y Carla estudia **Arquitectura**."
    },
    {
        "id": 2,
        "category": "👨‍👩‍👧‍👦 Parentesco y Conteo Mínimo",
        "question": "En una reunión familiar se encuentran presentes: 2 padres, 2 madres, 1 abuelo, 1 abuela, 1 tío, 1 tía, 1 hermano, 1 hermana, 1 sobrino, 1 sobrina, 1 nieto y 1 nieta. Si cada uno de ellos comió una porción de torta, ¿cuál es el mínimo número de porciones que se repartieron en total?",
        "options": [
            ("A", "A) 6"),
            ("B", "B) 7"),
            ("C", "C) 8"),
            ("D", "D) 10"),
            ("E", "E) 12")
        ],
        "correct": "A",
        "steps": [
            "1️⃣ **Generación 1 (Abuelos):** 1 Abuelo y 1 Abuela (2 personas casadas).",
            "2️⃣ **Generación 2 (Padres/Tíos):** Tienen 2 hijos (1 varón y 1 mujer, ambos casados o con pareja que cumplen roles de Padre/Madre/Tío/Tía).",
            "3️⃣ **Generación 3 (Nietos):** Cada uno tiene 1 hijo/hija (1 nieto varón y 1 nieta mujer).",
            "4️⃣ **Total acumulado:** 2 + 2 + 2 = **6 personas** que satisfacen simultáneamente los 12 roles solicitados."
        ],
        "visual_html": """
        <div style="background:#e0f2fe; padding:12px; border-radius:10px; text-align:center; font-weight:600; color:#0369a1; border:1px solid #bae6fd;">
            👴 Abuelo + 👵 Abuela (2 personas)<br>
            ↓<br>
            👨 Padre (Hijo) + 👩 Madre (Hija) (2 personas)<br>
            ↓<br>
            👦 Nieto + 👧 Nieta (2 personas)<br>
            <b>Mínimo total = 6 porciones de torta</b> 🍰
        </div>
        """,
        "summary": "El número mínimo de personas (y porciones de torta) es **6**."
    },
    {
        "id": 3,
        "category": "🔍 Verdades y Mentiras",
        "question": "Cuatro sospechosos de haber roto el vidrio de la biblioteca declaran ante el director:\n• Luis: 'Pedro lo hizo'\n• Pedro: 'Juan lo hizo'\n• Juan: 'Pedro miente'\n• Carlos: 'Yo no fui'\nSi se sabe que solo uno de ellos dice la verdad y que solo hay un culpable, ¿quién rompió el vidrio?",
        "options": [
            ("A", "A) Luis"),
            ("B", "B) Pedro"),
            ("C", "C) Juan"),
            ("D", "D) Carlos"),
            ("E", "E) Faltan datos")
        ],
        "correct": "D",
        "steps": [
            "1️⃣ **Analizar contradicciones:** Pedro afirma 'Juan lo hizo' y Juan responde 'Pedro miente'. Una de estas dos afirmaciones debe ser VERDADERA y la otra FALSA.",
            "2️⃣ **Regla del enunciado:** Únicamente HAY 1 VERDADERO entre los cuatro sospechosos.",
            "3️⃣ **Consecuencia lógica:** Como la verdad está entre Pedro o Juan, obligatoriamente Luis y Carlos MIENTEN.",
            "4️⃣ **Deducción del culpable:** La declaración de Carlos ('Yo no fui') es FALSA. Por lo tanto, el culpable es **Carlos**."
        ],
        "visual_html": """
        <div style="background:#fef3c7; padding:12px; border-radius:10px; color:#92400e; font-size:0.92rem; border:1px solid #fde68a;">
            📌 <b>Declaración de Carlos:</b> "Yo no fui" (FALSO ❌)<br>
            👉 Al ser falsa su afirmación, significa que <b>Carlos SÍ fue el culpable</b>.
        </div>
        """,
        "summary": "El culpable que rompió el vidrio es **Carlos**."
    },
    {
        "id": 4,
        "category": "🌳 Árbol Genealógico",
        "question": "Alberto es el padre de Beatriz. Carlos es el hijo de Fernando. Eduardo es el hermano de Carlos. Si se sabe que Beatriz es la madre de Eduardo, ¿qué parentesco tiene Fernando con Alberto?",
        "options": [
            ("A", "A) Su hijo"),
            ("B", "B) Su suegro"),
            ("C", "C) Su cuñado"),
            ("D", "D) Su nieto"),
            ("E", "E) Su yerno")
        ],
        "correct": "E",
        "steps": [
            "1️⃣ Beatriz es madre de Eduardo y Carlos.",
            "2️⃣ Fernando es padre de Carlos => Fernando y Beatriz son los padres/esposos.",
            "3️⃣ Alberto es el padre de Beatriz.",
            "4️⃣ El esposo de la hija de Alberto es su **yerno** (Fernando es el yerno de Alberto)."
        ],
        "visual_html": """
        <div style="background:#f3e8ff; padding:12px; border-radius:10px; text-align:center; color:#6b21a8; font-weight:600; border:1px solid #e9d5ff;">
            👴 Alberto (Padre de Beatriz)<br>
            ↓<br>
            👩 Beatriz 💍 👨 Fernando (Esposos)<br>
            ↓<br>
            👦 Carlos + 👦 Eduardo (Hijos)<br>
            <b>Fernando respecto a Alberto = Yerno</b>
        </div>
        """,
        "summary": "Fernando es el **yerno** de Alberto."
    },
    {
        "id": 5,
        "category": "📊 Matriz de Atributos",
        "question": "Tres profesionales (Pérez, Gómez y Ruiz) tienen diferentes profesiones (Médico, Abogado e Ingeniero) y viven en diferentes distritos (Lince, Surco y Ate). Se sabe que: Gómez no vive en Lince ni en Surco; El Abogado vive en Lince; El que vive en Surco no es Médico; Ruiz no es Abogado. ¿Qué profesión tiene Gómez y dónde vive Ruiz?",
        "options": [
            ("A", "A) Abogado – Surco"),
            ("B", "B) Ingeniero – Ate"),
            ("C", "C) Médico – Surco"),
            ("D", "D) Médico – Lince"),
            ("E", "E) Ingeniero – Lince")
        ],
        "correct": "C",
        "steps": [
            "1️⃣ **Distrito de Gómez:** Gómez no vive en Lince ni Surco => Gómez vive en **Ate**.",
            "2️⃣ **Abogado y Lince:** El abogado vive en Lince => Gómez no es abogado. Como el de Surco tampoco es médico => El de Surco es **Ingeniero**.",
            "3️⃣ **Profesión de Gómez:** Gómez vive en Ate y por descarte es **Médico**.",
            "4️⃣ **Ubicación de Ruiz:** Ruiz no es abogado => Ruiz vive en **Surco** y es **Ingeniero**. Pérez vive en Lince y es **Abogado**."
        ],
        "visual_html": """
        <table class="visual-table">
            <thead>
                <tr><th>Persona</th><th>Profesión</th><th>Distrito</th></tr>
            </thead>
            <tbody>
                <tr class="highlight-row"><td><b>Gómez</b></td><td><b>Médico (Respuesta)</b></td><td>Ate</td></tr>
                <tr class="highlight-row"><td><b>Ruiz</b></td><td>Ingeniero</td><td><b>Surco (Respuesta)</b></td></tr>
                <tr><td><b>Pérez</b></td><td>Abogado</td><td>Lince</td></tr>
            </tbody>
        </table>
        """,
        "summary": "Gómez es **Médico** y Ruiz vive en **Surco**."
    },
    {
        "id": 6,
        "category": "🧩 Acertijo de Relaciones",
        "question": "Una mujer va por la calle con un niño. Un conocido la detiene y le pregunta: '¿Quién es el niño?'. Ella responde: 'La madre de este niño es la hija de mi madre'. Si se sabe que la mujer que responde es hija única, ¿quién es el niño respecto a ella?",
        "options": [
            ("A", "A) Su hermano"),
            ("B", "B) Su sobrino"),
            ("C", "C) Su nieto"),
            ("D", "D) Su hijo"),
            ("E", "E) Su primo")
        ],
        "correct": "D",
        "steps": [
            "1️⃣ Analicemos la frase: 'La hija de mi madre'.",
            "2️⃣ Como la mujer es **hija única**, la única hija de su madre es **ella misma**.",
            "3️⃣ Reemplazamos en la oración: 'La madre de este niño soy **yo**'.",
            "4️⃣ Conclusión: El niño es **su hijo**."
        ],
        "visual_html": """
        <div style="background:#ecfdf5; padding:12px; border-radius:10px; text-align:center; color:#047857; font-weight:600; border:1px solid #a7f3d0;">
            "La hija de mi madre" = 👩 La propia mujer (Hija única)<br>
            "La madre del niño soy YO"<br>
            <b>El niño es su HIJO</b> 👶
        </div>
        """,
        "summary": "El niño es **su hijo**."
    },
    {
        "id": 7,
        "category": "🏢 Ordenamiento en Edificio",
        "question": "Seis amigos (A, B, C, D, E, F) viven en un edificio de 6 pisos, cada uno en un piso diferente:\n• B vive en el segundo piso.\n• C vive dos pisos más arriba que B.\n• A vive más arriba que D, pero más abajo que F.\n• E no vive en el primer piso ni en el último.\n• F y E viven en pisos adyacentes.\n¿En qué piso vive A?",
        "options": [
            ("A", "A) Primer piso"),
            ("B", "B) Segundo piso"),
            ("C", "C) Tercer piso"),
            ("D", "D) Cuarto piso"),
            ("E", "E) Quinto piso")
        ],
        "correct": "C",
        "steps": [
            "1️⃣ **Piso de B y C:** B vive en el Piso 2. C vive 2 pisos más arriba => Piso 2 + 2 = **Piso 4 (C)**.",
            "2️⃣ **Pisos vacíos iniciales:** {1, 3, 5, 6} disponibles para {A, D, E, F}.",
            "3️⃣ **Ubicación de E y F:** F y E viven juntos en pisos adyacentes. Como E no vive en el Piso 1 ni en el 6 (extremos), la única posición válida es **Piso 6 (F)** y **Piso 5 (E)**.",
            "4️⃣ **Ubicación de A y D:** Quedan los pisos 1 y 3. Como A vive más arriba que D => **A vive en el Piso 3** y **D en el Piso 1**."
        ],
        "visual_html": """
        <table class="visual-table">
            <thead>
                <tr>
                    <th style="width:20%;">Piso</th>
                    <th style="width:25%;">Habitante</th>
                    <th style="width:55%;">Explicación / Pista Aplicada</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><b>Piso 6</b></td>
                    <td><b style="font-size:1.1rem; color:#4338ca;">F</b></td>
                    <td>Adyacente a E (F en el último piso)</td>
                </tr>
                <tr>
                    <td><b>Piso 5</b></td>
                    <td><b style="font-size:1.1rem; color:#4338ca;">E</b></td>
                    <td>Adyacente a F (E no puede estar en los extremos 1 y 6)</td>
                </tr>
                <tr>
                    <td><b>Piso 4</b></td>
                    <td><b style="font-size:1.1rem; color:#4338ca;">C</b></td>
                    <td>2 pisos más arriba que B (Piso 2 + 2 = Piso 4)</td>
                </tr>
                <tr class="highlight-row">
                    <td><b>Piso 3</b></td>
                    <td><b style="font-size:1.2rem; color:#854d0e;">A (RESPUESTA)</b></td>
                    <td><b>A vive más arriba que D (Piso 3 > Piso 1)</b></td>
                </tr>
                <tr>
                    <td><b>Piso 2</b></td>
                    <td><b style="font-size:1.1rem; color:#4338ca;">B</b></td>
                    <td>Dato directo del enunciado (Piso 2)</td>
                </tr>
                <tr>
                    <td><b>Piso 1</b></td>
                    <td><b style="font-size:1.1rem; color:#4338ca;">D</b></td>
                    <td>Piso disponible restante (más abajo que A)</td>
                </tr>
            </tbody>
        </table>
        """,
        "summary": "A vive en el **Tercer piso**."
    },
    {
        "id": 8,
        "category": "🔗 Cadena de Parentescos",
        "question": "¿Qué parentesco tiene conmigo el padre del hermano del esposo de la única hermana de mi padre?",
        "options": [
            ("A", "A) Mi abuelo paterno"),
            ("B", "B) El consuegro de mi abuelo"),
            ("C", "C) Mi tío"),
            ("D", "D) Mi padre"),
            ("E", "E) Mi primo")
        ],
        "correct": "B",
        "steps": [
            "1️⃣ 'La única hermana de mi padre' = Mi tía paterna.",
            "2️⃣ 'El esposo de mi tía' = Mi tío político.",
            "3️⃣ 'El hermano del esposo de mi tía' = El hermano de mi tío político.",
            "4️⃣ 'El padre del hermano de mi tío político' = El padre de mi tío político.",
            "5️⃣ Relación con mi abuelo paterno: El padre de mi padre y el padre de mi tío político son **consuegros**."
        ],
        "visual_html": """
        <div style="background:#ffedd5; padding:12px; border-radius:10px; color:#c2410c; font-size:0.92rem; border:1px solid #fed7aa;">
            👨 Padreshare: Padre de mi tía (Mi abuelo) y Padre de su esposo (Consuegro de mi abuelo).<br>
            👉 Son los padres de una pareja de esposos = <b>Consuegros</b>.
        </div>
        """,
        "summary": "Es **el consuegro de mi abuelo**."
    },
    {
        "id": 9,
        "category": "🐱 Mascotas y Distritos",
        "question": "Cuatro personas (Hugo, Paco, Luis y Tito) tienen diferentes mascotas (Perro, Gato, Loro, Pez) y viven en diferentes distritos (San Miguel, Breña, Lince, Surco). Se sabe que: Hugo es alérgico a los perros y no vive en Surco; El que vive en Breña tiene el Perro; Luis vive en Lince y no tiene el Pez; El que vive en San Miguel no es Tito y tiene el Gato; Paco no vive en Breña. ¿Dónde vive Paco y qué mascota tiene Tito?",
        "options": [
            ("A", "A) Surco – Perro"),
            ("B", "B) San Miguel – Loro"),
            ("C", "C) Breña – Gato"),
            ("D", "D) Surco – Pez"),
            ("E", "E) Lince – Perro")
        ],
        "correct": "A",
        "steps": [
            "1️⃣ Breña tiene el Perro => Tito vive en Breña con el **Perro** (Hugo, Paco y Luis descartados de Breña).",
            "2️⃣ San Miguel tiene el Gato => Hugo vive en San Miguel con el **Gato**.",
            "3️⃣ Luis vive en Lince con el **Loro**.",
            "4️⃣ Paco vive en **Surco** con el **Pez**."
        ],
        "visual_html": """
        <table class="visual-table">
            <thead>
                <tr><th>Persona</th><th>Distrito</th><th>Mascota</th></tr>
            </thead>
            <tbody>
                <tr class="highlight-row"><td><b>Paco</b></td><td><b>Surco (Respuesta)</b></td><td>Pez</td></tr>
                <tr class="highlight-row"><td><b>Tito</b></td><td>Breña</td><td><b>Perro (Respuesta)</b></td></tr>
                <tr><td>Hugo</td><td>San Miguel</td><td>Gato</td></tr>
                <tr><td>Luis</td><td>Lince</td><td>Loro</td></tr>
            </tbody>
        </table>
        """,
        "summary": "Paco vive en **Surco** y Tito tiene el **Perro**."
    },
    {
        "id": 10,
        "category": "👑 Parentesco Político",
        "question": "Mi abuela tiene un solo hijo varón. Si la única hija de ese hijo es la madre de un niño, ¿qué parentesco tiene el padre de ese niño con el esposo de mi abuela?",
        "options": [
            ("A", "A) Su hijo"),
            ("B", "B) Su nieto"),
            ("C", "C) Su bisnieto"),
            ("D", "D) Su yerno"),
            ("E", "E) Su nieto político")
        ],
        "correct": "E",
        "steps": [
            "1️⃣ 'El único hijo varón de mi abuela' = Mi padre.",
            "2️⃣ 'La única hija de ese hijo' = Yo (o mi hermana).",
            "3️⃣ 'El padre de ese niño' = El esposo de la nieta.",
            "4️⃣ Respecto al esposo de mi abuela (mi abuelo), el esposo de su nieta es su **nieto político**."
        ],
        "visual_html": """
        <div style="background:#f0f9ff; padding:12px; border-radius:10px; text-align:center; color:#0369a1; font-weight:600; border:1px solid #bae6fd;">
            👴 Esposo de mi abuela (Mi Abuelo)<br>
            ↓<br>
            👧 Única hija de su hijo (Su Nieta)<br>
            ↓<br>
            👨 Padre del niño = 💍 Esposo de su nieta = <b>Nieto Político</b>
        </div>
        """,
        "summary": "El parentesco es **su nieto político**."
    }
]

# Helper function to get freshly shuffled questions
def get_shuffled_questions():
    shuffled = [dict(q) for q in BASE_QUESTIONS]
    random.shuffle(shuffled)
    return shuffled

# Initialize Session States
if "history" not in st.session_state:
    st.session_state.history = []

if "attempt_counter" not in st.session_state:
    st.session_state.attempt_counter = 1

if "active_questions" not in st.session_state:
    st.session_state.active_questions = get_shuffled_questions()

if "current_step" not in st.session_state:
    st.session_state.current_step = 0

if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}

if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

if "current_saved" not in st.session_state:
    st.session_state.current_saved = False

if "filter_mode" not in st.session_state:
    st.session_state.filter_mode = "ALL"

# Header Component
current_attempt_num = st.session_state.attempt_counter
st.markdown(f"""
<div class="main-header">
    <h1>Examen para Cinthia Paye</h1>
    <p>Cuestionario de Razonamiento Lógico & Parentescos Familiares</p>
    <div class="badge-container">
        <span class="badge">🔄 Intento Actual: #{current_attempt_num}</span>
        <span class="badge">📝 10 Preguntas (Orden Aleatorio)</span>
        <span class="badge">🎯 2 Pts por Pregunta</span>
        <span class="badge">🏆 Nota Máxima: 20 pts</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Main Navigation Tabs: Cuestionario vs Historial de Intentos
tab_quiz, tab_history = st.tabs(["📝 Cuestionario", "📜 Historial de Intentos"])

with tab_quiz:
    if not st.session_state.quiz_submitted:
        questions = st.session_state.active_questions
        current_q_idx = st.session_state.current_step
        q_data = questions[current_q_idx]

        # Progress calculation
        answered_count = len(st.session_state.user_answers)
        progress_val = (current_q_idx + 1) / len(questions)
        
        st.progress(progress_val)
        st.caption(f"Pregunta {current_q_idx + 1} de {len(questions)} | Respondidas: {answered_count}/{len(questions)}")

        # Category Pill & Question Header
        st.markdown(f'<div class="category-pill">{q_data["category"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="q-title">Pregunta {current_q_idx + 1} de {len(questions)} (ID #{q_data["id"]})</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="q-text">{q_data["question"]}</div>', unsafe_allow_html=True)

        # Options Radio
        option_keys = [opt[0] for opt in q_data["options"]]
        
        # Selected index if previously answered
        default_index = 0
        if q_data["id"] in st.session_state.user_answers:
            saved_ans = st.session_state.user_answers[q_data["id"]]
            if saved_ans in option_keys:
                default_index = option_keys.index(saved_ans)

        selected = st.radio(
            "Selecciona tu respuesta:",
            options=option_keys,
            format_func=lambda key: dict(q_data["options"])[key],
            index=default_index,
            key=f"q_radio_attempt{current_attempt_num}_q{q_data['id']}"
        )

        # Record answer
        st.session_state.user_answers[q_data["id"]] = selected

        st.markdown("---")

        # Step Navigation Buttons
        col_prev, col_center, col_next = st.columns([1, 1, 1])

        with col_prev:
            if current_q_idx > 0:
                if st.button("◀ Anterior", use_container_width=True):
                    st.session_state.current_step -= 1
                    st.rerun()

        with col_center:
            st.write("") # Spacer

        with col_next:
            if current_q_idx < len(questions) - 1:
                if st.button("Siguiente ▶", type="primary", use_container_width=True):
                    st.session_state.current_step += 1
                    st.rerun()
            else:
                if st.button("Finalizar Examen 🚀", type="primary", use_container_width=True):
                    st.session_state.quiz_submitted = True
                    st.session_state.current_saved = False
                    st.rerun()

    else:
        # Calculate Final Results for Current Attempt
        questions = st.session_state.active_questions
        total_questions = len(questions)
        correct_count = 0
        results_detail = []

        for q in questions:
            user_ans = st.session_state.user_answers.get(q["id"], None)
            is_correct = (user_ans == q["correct"])
            if is_correct:
                correct_count += 1
            
            results_detail.append({
                "question": q,
                "user_ans": user_ans,
                "is_correct": is_correct
            })

        score = correct_count * 2
        incorrect_count = total_questions - correct_count

        # Trigger Confetti Effect for high score!
        if score >= 16:
            st.balloons()

        # Save Attempt Record to History if not saved already
        if not st.session_state.current_saved:
            now_str = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            record = {
                "intento": st.session_state.attempt_counter,
                "timestamp": now_str,
                "score": score,
                "correct_count": correct_count,
                "incorrect_count": incorrect_count,
                "total": 20
            }
            st.session_state.history.append(record)
            st.session_state.attempt_counter += 1
            st.session_state.current_saved = True

        # Score Banner
        if score >= 16:
            card_class = "score-card-excelente"
            badge_msg = "🏆 ¡Excelente trabajo, Cinthia Paye!"
            sub_msg = "Demostraste un dominio extraordinario del razonamiento lógico."
        elif score >= 12:
            card_class = "score-card-bueno"
            badge_msg = "👏 ¡Muy Buen Resultado, Cinthia!"
            sub_msg = "Buen desempeño en la resolución de parentescos lógicos."
        else:
            card_class = "score-card-regular"
            badge_msg = "📚 ¡Sigue Practicando, Cinthia!"
            sub_msg = "Repasa el análisis detallado al final para reforzar tus conocimientos."

        st.markdown(f"""
        <div class="{card_class}">
            <h2 style="margin:0; font-size:1.6rem; color:white;">{badge_msg}</h2>
            <div class="score-number">{score} <span style="font-size:2rem; font-weight:600;">/ 20</span></div>
            <p style="font-size:1.1rem; color:white; margin:0;">{sub_msg}</p>
        </div>
        """, unsafe_allow_html=True)

        # Metrics Row
        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown(f"""
            <div class="metric-pill">
                <div class="metric-val" style="color: #10b981;">{correct_count}</div>
                <div class="metric-lbl">Aciertos (✅)</div>
            </div>
            """, unsafe_allow_html=True)

        with m2:
            st.markdown(f"""
            <div class="metric-pill">
                <div class="metric-val" style="color: #ef4444;">{incorrect_count}</div>
                <div class="metric-lbl">Fallos (❌)</div>
            </div>
            """, unsafe_allow_html=True)

        with m3:
            st.markdown(f"""
            <div class="metric-pill">
                <div class="metric-val" style="color: #6366f1;">{score} pts</div>
                <div class="metric-lbl">Puntaje Final</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("### 📊 Desglose y Resolución Dinámica Pregunta por Pregunta")
        st.write("Explora el enunciado completo, la resolución paso a paso y los esquemas visuales de cada acertijo:")

        # Filter buttons
        f_col1, f_col2, f_col3 = st.columns(3)
        with f_col1:
            if st.button("📋 Ver Todas", use_container_width=True, type="primary" if st.session_state.filter_mode == "ALL" else "secondary"):
                st.session_state.filter_mode = "ALL"
                st.rerun()
        with f_col2:
            if st.button("✅ Solo Aciertos", use_container_width=True, type="primary" if st.session_state.filter_mode == "RIGHT" else "secondary"):
                st.session_state.filter_mode = "RIGHT"
                st.rerun()
        with f_col3:
            if st.button("❌ Solo Fallos", use_container_width=True, type="primary" if st.session_state.filter_mode == "WRONG" else "secondary"):
                st.session_state.filter_mode = "WRONG"
                st.rerun()

        # Detailed Accordion Breakdown with Clean Single Statement Display
        for item in results_detail:
            is_corr = item["is_correct"]
            
            # Apply Filter
            if st.session_state.filter_mode == "RIGHT" and not is_corr:
                continue
            if st.session_state.filter_mode == "WRONG" and is_corr:
                continue

            q = item["question"]
            user_choice = item["user_ans"]
            
            status_icon = "✅" if is_corr else "❌"
            status_title = f"{status_icon} [{q['category']}] Pregunta #{q['id']}"
            
            with st.expander(status_title, expanded=(not is_corr)):
                # Full Question Callout (Displayed ONCE here cleanly)
                st.markdown(f"**📌 Enunciado Completo:**\n\n> {q['question']}")
                st.write("")

                opts_dict = dict(q["options"])
                user_str = opts_dict.get(user_choice, "Sin responder")
                correct_str = opts_dict.get(q["correct"], "")

                col_a, col_b = st.columns(2)
                with col_a:
                    if is_corr:
                        st.success(f"**Tu respuesta:** {user_str}")
                    else:
                        st.error(f"**Tu respuesta:** {user_str}")
                with col_b:
                    st.info(f"**Respuesta Correcta:** {correct_str}")

                # Creative Resolution Steps Box
                box_css = "resolution-box" if is_corr else "resolution-box-wrong"
                st.markdown(f'<div class="{box_css}">', unsafe_allow_html=True)
                st.markdown("💡 **Resolución Paso a Paso & Análisis Lógico:**")
                for s in q["steps"]:
                    st.markdown(f'<div class="step-box">{s}</div>', unsafe_allow_html=True)
                
                if "visual_html" in q:
                    st.markdown(q["visual_html"], unsafe_allow_html=True)
                
                st.markdown(f"<br>✨ <b>Conclusión:</b> {q['summary']}", unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("---")

        # Master Resolution Guide Section at the End of Quiz
        with st.expander("📘 Guía Master de Resolución Completa y Análisis Técnico (Paso a Paso)", expanded=False):
            st.markdown("""
            ### 🎓 Guía Oficial de Solución Lógica - Pool Completo (10 Preguntas)

            #### 1️⃣ Pregunta 1 (Mesa Circular)
            * **Enunciado Completo:** Cuatro amigas (Ana, Betty, Carla y Diana) se sientan alrededor de una mesa circular con 4 sillas distribuidas simétricamente. Se sabe que: Ana se sienta frente a la que estudia Derecho; Betty está a la derecha de la que estudia Medicina; Carla no estudia Derecho ni Medicina; Diana está frente a la que estudia Arquitectura; La que estudia Contabilidad está sentada frente a Betty. ¿Quién estudia Contabilidad y qué estudia Carla?
            * **Deducción:** Betty se ubica al Norte (Derecho), Ana al Sur (Contabilidad), Diana al Oeste (Medicina) y Carla al Este (Arquitectura).
            * **Respuesta:** **B) Ana – Arquitectura**

            #### 2️⃣ Pregunta 2 (Conteo Mínimo Familiar)
            * **Enunciado Completo:** En una reunión familiar se encuentran presentes: 2 padres, 2 madres, 1 abuelo, 1 abuela, 1 tío, 1 tía, 1 hermano, 1 hermana, 1 sobrino, 1 sobrina, 1 nieto y 1 nieta. Si cada uno de ellos comió una porción de torta, ¿cuál es el mínimo número de porciones que se repartieron en total?
            * **Deducción:** 3 generaciones compuestas por Abuelo+Abuela (2), Hijo+Hija (2) y Nieto+Nieta (2).
            * **Respuesta:** **A) 6 porciones de torta**

            #### 3️⃣ Pregunta 3 (Verdades y Mentiras)
            * **Enunciado Completo:** Cuatro sospechosos de haber roto el vidrio de la biblioteca declaran ante el director: Luis ('Pedro lo hizo'), Pedro ('Juan lo hizo'), Juan ('Pedro miente'), Carlos ('Yo no fui'). Si se sabe que solo uno de ellos dice la verdad y que solo hay un culpable, ¿quién rompió el vidrio?
            * **Deducción:** Pedro y Juan se contradicen, así que la única verdad está entre ellos. Por lo tanto, Carlos miente al decir "Yo no fui", significando que él rompió el vidrio.
            * **Respuesta:** **D) Carlos**

            #### 4️⃣ Pregunta 4 (Árbol Genealógico)
            * **Enunciado Completo:** Alberto es el padre de Beatriz. Carlos es el hijo de Fernando. Eduardo es el hermano de Carlos. Si se sabe que Beatriz es la madre de Eduardo, ¿qué parentesco tiene Fernando con Alberto?
            * **Deducción:** Beatriz y Fernando son los padres de Carlos y Eduardo. Como Alberto es el padre de Beatriz, Fernando es el cónyuge de su hija.
            * **Respuesta:** **E) Su yerno**

            #### 5️⃣ Pregunta 5 (Matriz de Atributos)
            * **Enunciado Completo:** Tres profesionales (Pérez, Gómez y Ruiz) tienen diferentes profesiones (Médico, Abogado e Ingeniero) y viven en diferentes distritos (Lince, Surco y Ate). Se sabe que: Gómez no vive en Lince ni en Surco; El Abogado vive en Lince; El que vive en Surco no es Médico; Ruiz no es Abogado. ¿Qué profesión tiene Gómez y dónde vive Ruiz?
            * **Deducción:** Gómez vive en Ate y es Médico. Ruiz vive en Surco y es Ingeniero. Pérez vive en Lince y es Abogado.
            * **Respuesta:** **C) Médico – Surco**

            #### 6️⃣ Pregunta 6 (Acertijo de Filiación)
            * **Enunciado Completo:** Una mujer va por la calle con un niño. Un conocido la detiene y le pregunta: '¿Quién es el niño?'. Ella responde: 'La madre de este niño es la hija de mi madre'. Si se sabe que la mujer que responde es hija única, ¿quién es el niño respecto a ella?
            * **Deducción:** "La hija de mi madre", siendo ella hija única, es la propia mujer. Por ende: "La madre del niño soy yo".
            * **Respuesta:** **D) Su hijo**

            #### 7️⃣ Pregunta 7 (Edificio de 6 Pisos - Tabla de Distribución)
            * **Enunciado Completo:** Seis amigos (A, B, C, D, E, F) viven en un edificio de 6 pisos, cada uno en un piso diferente: B vive en el 2° piso; C vive dos pisos más arriba que B; A vive más arriba que D, pero más abajo que F; E no vive en el 1° piso ni en el último; F y E viven en pisos adyacentes. ¿En qué piso vive A?
            * **Deducción:**
              * Piso 6: F (Adyacente a E)
              * Piso 5: E (Adyacente a F, no en los extremos 1 o 6)
              * Piso 4: C (2 pisos más arriba que B: 2 + 2 = 4)
              * **Piso 3: A (Respuesta: A vive más arriba que D)**
              * Piso 2: B (Dato del problema)
              * Piso 1: D (Piso libre restante)
            * **Respuesta:** **C) Tercer piso**

            #### 8️⃣ Pregunta 8 (Cadena de Parentescos)
            * **Enunciado Completo:** ¿Qué parentesco tiene conmigo el padre del hermano del esposo de la única hermana de mi padre?
            * **Deducción:** El padre del hermano del esposo de mi tía es el padre de mi tío político. Relacionado con el padre de mi tía (mi abuelo), son los padres de un matrimonio.
            * **Respuesta:** **B) El consuegro de mi abuelo**

            #### 9️⃣ Pregunta 9 (Mascotas y Distritos)
            * **Enunciado Completo:** Cuatro personas (Hugo, Paco, Luis y Tito) tienen diferentes mascotas (Perro, Gato, Loro, Pez) y viven en diferentes distritos (San Miguel, Breña, Lince, Surco). Se sabe que: Hugo es alérgico a los perros y no vive en Surco; El que vive en Breña tiene el Perro; Luis vive en Lince y no tiene el Pez; El que vive en San Miguel no es Tito y tiene el Gato; Paco no vive en Breña. ¿Dónde vive Paco y qué mascota tiene Tito?
            * **Deducción:** Tito (Breña-Perro), Hugo (San Miguel-Gato), Luis (Lince-Loro), Paco (Surco-Pez).
            * **Respuesta:** **A) Surco – Perro**

            #### 🔟 Pregunta 10 (Parentesco Político)
            * **Enunciado Completo:** Mi abuela tiene un solo hijo varón. Si la única hija de ese hijo es la madre de un niño, ¿qué parentesco tiene el padre de ese niño con el esposo de mi abuela?
            * **Deducción:** El único hijo varón de mi abuela es mi padre. Su hija es mi hermana/yo (nieta del abuelo). El padre del niño es el esposo de la nieta.
            * **Respuesta:** **E) Su nieto político**
            """)

        st.markdown("---")

        # Restart Quiz Button with Shuffled Order
        if st.button("🔄 Nuevo Intento (Preguntas en Orden Aleatorio)", type="primary", use_container_width=True):
            st.session_state.active_questions = get_shuffled_questions()
            st.session_state.current_step = 0
            st.session_state.user_answers = {}
            st.session_state.quiz_submitted = False
            st.session_state.current_saved = False
            st.session_state.filter_mode = "ALL"
            st.rerun()

with tab_history:
    st.markdown("### 📜 Historial de Intentos de Cinthia Paye")
    
    if not st.session_state.history:
        st.info("Aún no hay intentos registrados. Completa el cuestionario para registrar tu primer intento.")
    else:
        st.write(f"Total de intentos realizados hasta el momento: **{len(st.session_state.history)}**")
        
        # Display Attempts Table / Cards
        for rec in reversed(st.session_state.history):
            pct = int((rec["score"] / rec["total"]) * 100)
            badge_color = "#10b981" if rec["score"] >= 16 else ("#3b82f6" if rec["score"] >= 12 else "#f59e0b")
            
            st.markdown(f"""
            <div style="background: white; border-radius: 16px; padding: 1.2rem 1.5rem; border: 1px solid #e2e8f0; margin-bottom: 1rem; box-shadow: 0 2px 5px rgba(0,0,0,0.03);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                    <span style="font-weight: 700; font-size: 1.1rem; color: #1e293b;">Intento #{rec['intento']}</span>
                    <span style="background: {badge_color}; color: white; padding: 4px 12px; border-radius: 12px; font-weight: 700; font-size: 0.9rem;">{rec['score']} / 20 pts ({pct}%)</span>
                </div>
                <div style="display: flex; gap: 15px; font-size: 0.9rem; color: #64748b;">
                    <span>🕒 {rec['timestamp']}</span>
                    <span>✅ Aciertos: {rec['correct_count']}</span>
                    <span>❌ Fallos: {rec['incorrect_count']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    # Protected History Deletion Section with PIN
    with st.expander("🔐 Administrar y Eliminar Historial de Intentos"):
        st.warning("⚠️ **Zona Restringida:** Eliminar el historial borrará permanentemente todos los registros de intentos.")
        
        pin_input = st.text_input("Ingrese el PIN de seguridad para eliminar:", type="password", key="delete_pin_input")
        
        if st.button("🗑️ Eliminar Todo el Historial", type="primary"):
            if pin_input == "0208":
                st.session_state.history = []
                st.session_state.attempt_counter = 1
                st.success("✅ Historial de intentos eliminado correctamente.")
                st.rerun()
            else:
                st.error("❌ PIN incorrecto. Acceso denegado.")
