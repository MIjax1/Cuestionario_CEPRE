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

# Custom CSS for Modern, Sleek Visual Presentation
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
        margin-bottom: 0.4rem;
    }

    .q-text {
        font-size: 1.25rem;
        font-weight: 600;
        line-height: 1.45;
        color: #1f2937;
        margin-bottom: 1.2rem;
    }

    .stRadio > label {
        font-weight: 600;
        font-size: 1rem;
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

    /* Primary buttons custom style */
    div.stButton > button {
        border-radius: 12px;
        font-weight: 600;
        padding: 0.5rem 1.5rem;
        transition: all 0.2s ease;
    }

    .history-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 1rem 1.2rem;
        margin-bottom: 0.8rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
</style>
""", unsafe_allow_html=True)

# Master Question Pool Definition
BASE_QUESTIONS = [
    {
        "id": 1,
        "title": "PREGUNTA 1",
        "question": "¿Qué parentesco tiene conmigo el hijo de la hermana de mi padre?",
        "options": [
            ("a", "a) Mi tío"),
            ("b", "b) Mi hermano"),
            ("c", "c) Mi primo"),
            ("d", "d) Mi sobrino"),
            ("e", "e) Mi cuñado")
        ],
        "correct": "c",
        "analysis": "La hermana de mi padre es mi tía; el hijo de mi tía es mi primo."
    },
    {
        "id": 2,
        "title": "PREGUNTA 2",
        "question": "En una cena familiar se encuentran 2 padres y 2 hijos. ¿Cuál es el menor número de personas que puede haber en dicha cena?",
        "options": [
            ("a", "a) 2"),
            ("b", "b) 3"),
            ("c", "c) 4"),
            ("d", "d) 5"),
            ("e", "e) 6")
        ],
        "correct": "b",
        "analysis": "Para el mínimo de personas, asume una línea recta de 3 integrantes: Abuelo, Padre e Hijo. Hay 2 padres (abuelo y padre) y 2 hijos (padre e hijo)."
    },
    {
        "id": 3,
        "title": "PREGUNTA 3",
        "question": "¿Qué parentesco tiene conmigo el abuelo paterno de la hija de mi único hermano?",
        "options": [
            ("a", "a) Mi abuelo"),
            ("b", "b) Mi padre"),
            ("c", "c) Mi tío"),
            ("d", "d) Mi hermano"),
            ("e", "e) Yo mismo")
        ],
        "correct": "b",
        "analysis": "La hija de mi hermano es mi sobrina; el abuelo paterno de mi sobrina es el padre de mi hermano, o sea, mi padre."
    },
    {
        "id": 4,
        "title": "PREGUNTA 4",
        "question": "Si la mamá de Juana es la hermana de mi hermano gemelo, ¿qué es respecto a mí el abuelo del mellizo de Juana?",
        "options": [
            ("a", "a) Mi abuelo"),
            ("b", "b) Mi hermano"),
            ("c", "c) Mi padre"),
            ("d", "d) Mi tío"),
            ("e", "e) Mi cuñado")
        ],
        "correct": "c",
        "analysis": "La hermana de mi gemelo es mi hermana; su mellizo es su otro hijo, o sea mi sobrino. El abuelo de mi sobrino es mi padre."
    },
    {
        "id": 5,
        "title": "PREGUNTA 5",
        "question": "Una familia está compuesta por 3 padres, 3 hijos, 2 abuelos y 2 nietos. ¿Cuál es el menor número de personas que conforman dicha familia?",
        "options": [
            ("a", "a) 4"),
            ("b", "b) 5"),
            ("c", "c) 6"),
            ("d", "d) 7"),
            ("e", "e) 8")
        ],
        "correct": "a",
        "analysis": "Línea de 4 generaciones: Bisabuelo, Abuelo, Padre, Hijo. Cumplen todos los roles requeridos con solo 4 personas."
    },
    {
        "id": 6,
        "title": "PREGUNTA 6",
        "question": "¿Qué parentesco tiene conmigo el hijo de la esposa del único vástago (hijo) de mi abuela?",
        "options": [
            ("a", "a) Mi primo"),
            ("b", "b) Mi tío"),
            ("c", "c) Mi sobrino"),
            ("d", "d) Soy yo mismo o mi hermano"),
            ("e", "e) Mi abuelo")
        ],
        "correct": "d",
        "analysis": "El único vástago de mi abuela es mi padre/madre. La esposa de él es mi madre. El hijo de mi madre soy yo mismo o mi hermano."
    },
    {
        "id": 7,
        "title": "PREGUNTA 7",
        "question": "En una reunión familiar están presentes: 2 esposos, 2 esposas, 2 padres, 2 madres, 1 suegro, 1 suegra, 1 nuera, 1 hijo y 1 nieto. ¿Cuántas personas como mínimo hay en la reunión?",
        "options": [
            ("a", "a) 4"),
            ("b", "b) 5"),
            ("c", "c) 6"),
            ("d", "d) 7"),
            ("e", "e) 8")
        ],
        "correct": "b",
        "analysis": "Son los abuelos casados (2 personas) y el hijo de ellos casado con su esposa (2 personas), más el nieto (1 persona). Suman 5 y cumplen exactamente todos los roles."
    },
    {
        "id": 8,
        "title": "PREGUNTA 8",
        "question": "Tomás es el único hijo del abuelo de Rafael, y Rosario es la única nuera del abuelo de Rafael. Si el hijo único de Tomás tiene 5 años, ¿qué parentesco une a Rafael y Rosario?",
        "options": [
            ("a", "a) Tía y sobrino"),
            ("b", "b) Madre e hijo"),
            ("c", "c) Esposos"),
            ("d", "d) Hermanos"),
            ("e", "e) Abuela y nieto")
        ],
        "correct": "b",
        "analysis": "Tomás es el padre de Rafael y Rosario es la esposa de Tomás. Por lo tanto, Rosario es la madre de Rafael."
    },
    {
        "id": 9,
        "title": "PREGUNTA 9",
        "question": "Si el hijo de Juan es el padre de mi hijo, ¿qué parentesco tengo yo con Juan, si se sabe que soy hombre?",
        "options": [
            ("a", "a) Su hermano"),
            ("b", "b) Su padre"),
            ("c", "c) Su nieto"),
            ("d", "d) Su tío"),
            ("e", "e) Su hijo")
        ],
        "correct": "e",
        "analysis": "'El padre de mi hijo' soy yo mismo. Reemplazando en la oración: 'El hijo de Juan soy yo'."
    },
    {
        "id": 10,
        "title": "PREGUNTA 10",
        "question": "Mi nombre es Daniel. ¿Qué parentesco tiene conmigo el tío del hijo del único hermano de mi padre?",
        "options": [
            ("a", "a) Mi hermano"),
            ("b", "b) Mi tío"),
            ("c", "c) Mi abuelo"),
            ("d", "d) Mi padre"),
            ("e", "e) Mi primo")
        ],
        "correct": "d",
        "analysis": "El único hermano de mi padre es mi tío; su hijo es mi primo; el tío de mi primo es mi padre."
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

        # Question Header and Text
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

        st.markdown("### 📊 Desglose y Análisis Pregunta por Pregunta")
        st.write("Revisa en qué preguntas acertaste y en cuáles fallaste, junto a la explicación lógica de cada una:")

        # Detailed Accordion Breakdown
        for item in results_detail:
            q = item["question"]
            is_corr = item["is_correct"]
            user_choice = item["user_ans"]
            
            status_icon = "✅" if is_corr else "❌"
            status_title = f"{status_icon} {q['question']}"
            
            with st.expander(status_title, expanded=(not is_corr)):
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

                st.markdown(f"💡 **Análisis / Justificación:**\n{q['analysis']}")

        st.markdown("---")

        # Restart Quiz Button with Shuffled Order
        if st.button("🔄 Nuevo Intento (Preguntas en Orden Aleatorio)", type="primary", use_container_width=True):
            st.session_state.active_questions = get_shuffled_questions()
            st.session_state.current_step = 0
            st.session_state.user_answers = {}
            st.session_state.quiz_submitted = False
            st.session_state.current_saved = False
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
