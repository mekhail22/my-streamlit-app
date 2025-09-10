import streamlit as st
import base64

st.markdown(
    """
    <style>
        .top-buttons {
            position: fixed;
            top: 70px;
            right: 100px;
            z-index: 100;
        }
        .top-buttons a {
            text-decoration: none;
            margin-left: 10px;
        }
        .top-buttons button {
            font-size: 16px;
            padding: 8px 18px;
            background-color: #6C81A9;
            color:black;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }
    </style>
    <div class="top-buttons">
        <a href='?page=10' target="_self"><button>Contact Us</button></a>
        <a href='?page=11' target="_self"><button>About Us</button></a>
    </div>
    """,
    unsafe_allow_html=True
)

# تحويل الصورة لـ base64
def img_to_base64(img_path):
    with open(img_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

logo_base64 = img_to_base64("logo.png")

# عرض الصورة فوق الشمال دايمًا مع رابط للصفحة الأولى
st.markdown(
    f"""
    <style>
        .top-left-img {{
            position: fixed;
            top: 10px;
            left: 10px;
            width: 200px;
            cursor: pointer;
            z-index: 100;
        }}
    </style>
    <a href='?page=1' target="_self">
        <img src="data:image/png;base64,{logo_base64}" class='top-left-img'>
    </a>
    """,
    unsafe_allow_html=True
)


# -------------------------------------------
# دالة لتحويل الصور Base64 (للاستخدام في الخلفية)
def img_to_base64(img_path):
    with open(img_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# -------------------------------------------
# إعداد الصفحة
st.set_page_config(page_title="مسكونيات", page_icon="✝️", layout="wide")

# -------------------------------------------
# الخلفية (صورة واحدة موحدة لكل الصفحات)
bg_img = img_to_base64("mgma8.png")  # غيّر اسم الصورة حسب اللي عندك

st.markdown(
    f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background: url("data:image/png;base64,{bg_img}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    [data-testid="stHeader"], [data-testid="stSidebar"] {{
        background: rgba(0,0,0,0);  /* شفاف */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------
# إدارة الصفحات بالـ query params
query_params = st.query_params
if "page" not in query_params:
    query_params["page"] = "1"

page = int(query_params["page"])

# -------------------------------------------------------------------
# الصفحة الأولى
if page == 1:
    st.markdown(
        """<h1 style='direction:rtl; text-align:right; color:black;'>يعني إيه مجامع المسكونية</h1>""",
        unsafe_allow_html=True
    )

    html_spaced_text = """معناه اجتماع رعاة ومعلمي الكنيسة من جميع جهات المسكونة "العالم"، 
    لمناقشة أمر يخص الإيمان المسيحي، بهدف حفظ النظام وسلامة العقيدة بين المسيحيين في شتى أنحاء العالم. 
    ويقترب هذا المصطلح من تعبير "مؤتمر دولي"، ولكنه لا يخص الدول، بل الكنائس المسيحية في البلدان المختلفة. 
    يجتمع الأساقفة في العالم لدراسة المشاكل الإيمانية والرعوية."""

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("mgma4.jpg", width=400)
    with col2:
        st.markdown(
            f"<p style='font-size:28px; line-height:1.9; direction:rtl; text-align:right; color:black;'>{html_spaced_text}</p>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"""
            <div style='text-align:right; position:relative; top:240px;'>
                <a href="?page=2"target="_self">
                    <button style='font-size:20px; padding:10px 25px; background-color:#4CAF50; color:black; border:none; border-radius:8px; cursor:pointer;'>
                        التالي
                    </button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

# -------------------------------------------------------------------
# الصفحة الثانية
elif page == 2:
    st.markdown(
        "<h1 style='text-align: center; color:black;'>مجامع المسكونية عبر التاريخ</h1>",
        unsafe_allow_html=True
    )

    images = [
        ("mgma1.png", "مجمع افسس تأسس عام ٤٣١م", "?page=3"),
        ("mgma2.jpg", "مجمع القسطنطينية تأسس عام ٣٨١م", "?page=6"),
        ("mgma3.jpg", "مجمع نيقية تأسس عام ٣٢٥م", "?page=9")
    ]

    def img_to_base64(img_path):
        with open(img_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

    st.markdown("""
    <style>
    .zoom-img {
        transition: transform 0.3s ease;
        cursor: pointer;
    }
    .zoom-img:hover {
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)

    cols = st.columns(len(images))
    for col, (img_path, title, link_url) in zip(cols, images):
        with col:
            img_base64 = img_to_base64(img_path)
            st.markdown(
                f"""
                <div style='text-align:center;'>
                    <a href="{link_url}"target="_self">
                        <img src="data:image/png;base64,{img_base64}" 
                             class="zoom-img" width="300" height="300" 
                             style="object-fit:cover; border-radius:15px;">
                    </a>
                    <div style='font-size:26px; margin-top:10px; color:black;'>{title}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
    st.markdown(
    """
    <div style='text-align:left; margin-top:100px; margin-left:-50px;'>
        <a href="?page=1" target="_self">
            <button style='font-size:20px; padding:10px 25px; background-color:#f44336; color:black; border:none; border-radius:8px; cursor:pointer;'>
                رجوع
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------------------------
# الصفحة الثالثة
elif page == 3:
    st.markdown(
        "<h1 style='direction:rtl; text-align:right; color:black;'>مجمع أفسس</h1>",
        unsafe_allow_html=True
    )

    html_text = """استمر الأريوسيون بعد مجمع القسطنطينية، في الهجوم على العقيدة الأرثوذكسية، وظهر في أنطاكيا واعظ قدير، ولد في قيصرية سوريا، ثم أتى إلى أنطاكيا في سن مبكرة والتحق بدير إفربيوس، ومن هناك عيِّن شماسًا ثم قسيسًا في كاتدرائية أنطاكيا. ونتيجة للشهرة التي نالها في دفاعه ضد الأريوسية اُختير ليصير أسقفًا للقسطنطينية في 10 أبريل 428 م.، وترجى شعب القسطنطينية أن يجدوا فيه خلفًا ليوحنا ذهبي الفم. وقد جاء هذا البطريرك من مدرسة ثيئودوروس الموبسويستي ودُعي هذا البطريرك باسم نسطور خلفًا لبطريرك القسطنطينية الذي انتقل في 24 ديسمبر 427 م."""
    html_text2 = """وفي عظته الأولى التي يسمونها خطبة العرش خاطب الإمبراطور ثيئودوسيوس الصغير بالكلمات التالية: "أعطيني أيها الإمبراطور الأرض نقية من الهراطقة وأنا سوف أعطيك السماء، ساعدني لأشن حربًا ضد الهراطقة وأنا سوف أساعدك في حربك ضد الفرس"."""
    html_text3 = """وكان الأريوسيون يهاجمون التعليم الأرثوذكسي كما يلي: يقولون أن الكنيسة تنسب إلى الله -جلت قدرته- الموت والآلام والولادة من امرأة ويعتبرون هذا كفرًا وأن الله لم يكن له كفوًا أحد."""

    col_img, col_text = st.columns([1, 2])
    with col_img:
        st.image("mgma5.jpg", width=400)
    with col_text:
        for text in [html_text, html_text2, html_text3]:
            st.markdown(
                f"<p style='font-size:28px; line-height:1.9; direction:rtl; text-align:right; color:black;'>{text}</p>",
                unsafe_allow_html=True
            )

    col_left, col_spacer, col_right = st.columns([1, 8, 1])
    with col_left:
        st.markdown(
            """
            <div style='text-align:left;'>
                <a href="?page=2"target="_self">
                    <button style='font-size:20px; padding:10px 25px; background-color:#f44336; color:black; border:none; border-radius:8px; cursor:pointer;'>
                        رجوع
                    </button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col_right:
        st.markdown(
            """
            <div style='text-align:right;'>
                <a href="?page=4"target="_self">
                    <button style='font-size:20px; padding:10px 25px; background-color:#4CAF50; color:black; border:none; border-radius:8px; cursor:pointer;'>
                        التالي
                    </button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

# -------------------------------------------------------------------
# الصفحة الرابعة
elif page == 4:
    st.markdown(
        """<h1 style='direction:rtl; text-align:right; color:black;'>مجمع افسس</h1>""",
        unsafe_allow_html=True
    )

    html_text = """نسطور حاول يواجه الأريوسية، فشدّد على ألوهية ابن الله وقال إن اللوغوس لا يموت ولا يتألم. لكنه رفض فكرة أن اللوغوس اتحد فعلًا بجسد إنساني. اعتقد أن الله اختار إنسانًا من بطن العذراء مريم ليسكن فيه ويعطيه الكرامة والألقاب والسلطان. ومن هنا رأى أن المسيح مجرد إنسان رافقه اللوغوس."""
    html_text2 = """قال أيضًا إن يسوع ورث الخطية الأصلية، وإنه قدَّم نفسه ذبيحة عن نفسه وعن العالم. وأصر أن الذي وُلد من مريم هو إنسان فقط، لذلك رفض أن تُدعى العذراء والدة الإله، وابتكر لقب "والدة المسيح". فسَّر الاتحاد بين اللاهوت والناسوت على أنه مجرد اتحاد في الكرامة والشرف، لا في الطبيعة. واعتبر أن اللوغوس فارق جسد يسوع على الصليب، وبالتالي فالمسيح عنده شخصان: إله وإنسان يُعبدان معًا. بهذا التعليم لم يحل نسطور مشكلة الأريوسية، بل زادها تعقيدًا، لأنه أنكر ألوهية المسيح الحقيقية وقدّم صورة مشوهة للإيمان المسيحي."""

    col_img, col_text = st.columns([1, 2])
    with col_img:
        st.image("mgma6.jpg", width=500)
    with col_text:
        for text in [html_text, html_text2]:
            st.markdown(
                f"<p style='font-size:28px; line-height:1.9; direction:rtl; text-align:right; color:black;'>{text}</p>",
                unsafe_allow_html=True
            )

    col_left, col_right = st.columns([1, 2])
    with col_left:
        st.markdown(
            """
            <div style='text-align:left;'>
                <a href="?page=3"target="_self">
                    <button style='font-size:20px; padding:10px 25px; background-color:#f44336; color:black; border:none; border-radius:8px; cursor:pointer;'>
                        رجوع
                    </button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col_right:
        st.markdown(
            """
            <div style='text-align:right;'>
                <a href="?page=5"target="_self">
                    <button style='font-size:20px; padding:10px 25px; background-color:#4CAF50; color:black; border:none; border-radius:8px; cursor:pointer;'>
                        التالي
                    </button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
# -------------------------------------------------------------------
# صفحه الخامسه
elif page == 5:
    st.markdown(
        "<h1 style='direction:rtl; text-align:right; color:black;'>مجمع أفسس</h1>",
        unsafe_allow_html=True
    )

    html_text1 = """القديس كيرلس الكبير وضّح إن الله الكلمة أخذ طبيعة إنسانية كاملة بلا خطية، واتحد بيها في شخصه هو نفسه. يعني لما يتألم، يتألم بجسده، ولما يموت، يموت بحسب إنسانيته، لكن لاهوته ما يتأثرش. لذلك نقول إن الله الكلمة مات بالجسد، لكن مش إن لاهوته مات."""
    html_text2 ="""زي المثال البسيط: لو شخص اسمه جرجس انضرب جسده، نقول "جرجس انضرب"، مع إن اللي اتضرب هو جسده مش روحه. نفس الفكرة مع المسيح: لما صُلب، اللي صُلب هو جسده المتحد باللاهوت، لكن الشخص هو الله الكلمة."""
    html_text3 ="""ومن هنا نقول إن العذراء ولدت الله الكلمة، لأنه هو نفسه اللي اتجسد منها، لكن لاهوته ما ابتداش منها لأنه من الأزل مولود من الآب. علشان كده الكنيسة بتسميها "والدة الإله".الله الكلمة له ميلادان: الأول من الآب قبل كل الدهور بحسب لاهوته، والتاني من العذراء في ملء الزمان بحسب ناسوته"""
    col_img, col_text = st.columns([1, 2])
    with col_img:
        st.image("mgma7.jpg", width=400)
    with col_text:
        st.markdown(
            f"<p style='font-size:28px; line-height:1.9; direction:rtl; text-align:right; color:black;'>{html_text1}</p>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<p style='font-size:28px; line-height:1.9; direction:rtl; text-align:right; color:black;'>{html_text2}</p>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<p style='font-size:28px; line-height:1.9; direction:rtl; text-align:right; color:black;'>{html_text3}</p>",
            unsafe_allow_html=True
        )
    st.markdown(
        """
        <div style='text-align:left;'>
            <a href="?page=4"target="_self">
                <button style='font-size:20px; padding:10px 25px; background-color:#f44336; color:black; border:none; border-radius:8px; cursor:pointer;'>
                    رجوع
                </button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
# -------------------------------------------------------------------
#الصفحه الساته
elif page == 6:
    st.markdown(
        "<h1 style='direction:rtl; text-align:right; color:black;'>مجمع لقسطنطينية</h1>",
        unsafe_allow_html=True
    )

    html_text1 = """مقدونيوس، بطريرك القسطنطينية، أنكر ألوهية الروح القدس وقال إنه أقل من الابن لأنه "لا يتكلم من نفسه بل يأخذ مما للابن ويخبر". لكن القديس كيرلس وآباء الكنيسة ردوا إن ده فهم خاطئ، لأن حتى الابن قال عن نفسه إنه "لا يقدر أن يعمل من نفسه شيئًا إلا ما ينظر الآب يعمل". المعنى إن الأقانيم الثلاثة لا يعمل واحد منهم منفصلًا عن الآخرين، لكنهم واحد في الجوهر والعمل."""
    html_text2="""الروح القدس إذًا مش أقل من الابن، بل يعمل في انسجام كامل مع الآب والابن. وكونه "يأخذ مما للابن" معناه إنه يشهد للمسيح ويعلن أنه ابن الله المولود من الآب قبل كل الدهور، عشان يمنع أي روح كاذب أو نبي مزيف من ادعاء أنه يتكلم بالروح القدس.الآباء وضحوا إن الروح القدس يعلن لنا عمل المسيح ويكمل العطايا فينا، لكن ده لا ينقص من ألوهيته، بل يؤكد وحدانيته مع الآب والابن."""
    col_img, col_text = st.columns([1, 2])
    with col_img:
        st.image("mgma9.jpg", width=400)
    with col_text:
        st.markdown(
            f"<p style='font-size:28px; line-height:1.9; direction:rtl; text-align:right; color:black;'>{html_text1}</p>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<p style='font-size:28px; line-height:1.9; direction:rtl; text-align:right; color:black;'>{html_text2}</p>",
            unsafe_allow_html=True
        )
    st.markdown(
        """
        <div style='text-align:left;margin-top:50px; margin-left:-50px'>
            <a href="?page=2"target="_self">
                <button style='font-size:20px; padding:10px 25px; background-color:#f44336; color:black; border:none; border-radius:8px; cursor:pointer;'>
                    رجوع
                </button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
            """
            <div style='text-align:right;margin-top:-50px'>
                <a href="?page=7"target="_self">
                    <button style='font-size:20px; padding:10px 25px; background-color:#4CAF50; color:black; border:none; border-radius:8px; cursor:pointer;'>
                        التالي
                    </button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
# -------------------------------------------------------------------
#الصفحه السابعه
elif page ==7 :
    st.markdown(
        "<h1 style='direction:rtl; text-align:right; color:black;'>مجمع قسطنطينية</h1>",
        unsafe_allow_html=True
    )

    html_text1 = """الكتاب المقدس بيعلن إن الروح القدس هو الله نفسه، الخالق، زي ما اتقال "روح الله صنعني" في أيوب، والمزمور بيقول "أين أذهب من روحك" علشان يوضح إنه حاضر في كل مكان. والقديس بطرس كمان وضّح إن الكذب على الروح القدس هو كذب على الله، وده بيثبت ألوهيته."""
    html_text2 ="""المسيح لما اتكلم عن الروح القدس، قال إنه "معزّي آخر"، يعني شخص حقيقي ليه أقنومه الخاص، مش مجرد قوة أو طاقة. وبيتكلم عنه بأفعال واضحة: يسمع، يتكلم، يشهد، يأخذ، ويمجد المسيح، ودي كلها صفات شخص حي، مش طاقة جامدة.زي ما الابن ليه شخصيته الحقيقية كابن الله، الروح القدس كمان ليه شخصيته الخاصة. هو اللي بيقود الكنيسة، ويشتغل في الأسرار، ويشهد للمسيح دايمًا.علشان كده الآباء أكدوا إن الروح القدس مساوي للآب والابن في الجوهر، وإنه أقنوم حقيقي ليه شخصيته المتمايزة. وبالمجمع المسكوني التاني في القسطنطينية سنة 381، الكنيسة أعلنت بوضوح ألوهيته ورفضت تعليم مقدونيوس اللي كان بينكر ده"""
    col_img, col_text = st.columns([1, 2])
    with col_img:
        st.image("mgma9.jpg", width=400)
    with col_text:
        st.markdown(
            f"<p style='font-size:28px; line-height:1.9; direction:rtl; text-align:right; color:black;'>{html_text1}</p>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<p style='font-size:28px; line-height:1.9; direction:rtl; text-align:right; color:black;'>{html_text2}</p>",
            unsafe_allow_html=True
        )
    st.markdown(
    """
    <div style='text-align:left; margin-top:50px; margin-left:-50px;'>
        <a href="?page=6" target="_self">
            <button style='font-size:20px; padding:10px 25px; background-color:#f44336; color:black; border:none; border-radius:8px; cursor:pointer;'>
                رجوع
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

    
    st.markdown(
            """
            <div style='text-align:right;margin-top:-50px'>
                <a href="?page=8"target="_self">
                    <button style='font-size:20px; padding:10px 25px; background-color:#4CAF50; color:black; border:none; border-radius:8px; cursor:pointer;'>
                        التالي
                    </button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
# -------------------------------------------------------------------
#الصفحه التامنه
elif page ==8:
    st.markdown(
        "<h1 style='direction:rtl; text-align:right; color:black;'>مجمع قسطنطينية</h1>",
        unsafe_allow_html=True
    )

    html_text1 = """أبوليناريوس كان عايز يحافظ على وحدة المسيح وما يبقاش فيه شخصين، فقرر يلغي وجود الروح الإنساني العاقل عند المسيح، وقال إن لاهوت الكلمة هو اللي يقوم بدوره. كده كان قصده يحل مشكلة لكنه وقع في خطأ كبير، لأنه أنكر كمال ناسوت المسيح."""
    html_text2 ="""في المقابل، نسطور وقع في العكس، ففصل المسيح لطبيعتين منفصلتين، وده برضه غلط. الغريب إن الاتنين رغم اختلافهم وصلوا لنفس المشكلة، لأنهم بدأوا من نفس الفكرة الغلط: إن وجود روح إنساني عاقل للمسيح معناه إنه شخص مستقل.لكن إيمان الكنيسة واضح: المسيح شخص واحد، هو الله الكلمة المتجسد، اللي أخد طبيعة بشرية كاملة بجسد وروح عاقل، من غير ما ينقسم لشخصين. وده اللي أكده القديس أثناسيوس وكيرلس الكبير."""
    col_img, col_text = st.columns([1, 2])
    with col_img:
        st.image("mgma10.jpg", width=600)
    with col_text:
        st.markdown(
            f"<p style='font-size:28px; line-height:1.9; direction:rtl; text-align:right; color:black;'>{html_text1}</p>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<p style='font-size:28px; line-height:1.9; direction:rtl; text-align:right; color:black;'>{html_text2}</p>",
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <div style='text-align:left;margin-left:-500px'>
                <a href="?page=7"target="_self">
                    <button style='font-size:20px; padding:10px 25px; background-color:#f44336; color:black; border:none; border-radius:8px; cursor:pointer;'>
                        رجوع
                    </button>
                </a>
            </div>
            """,
            unsafe_allow_html=True)
# -------------------------------------------------------------------
#الصفحه التاسعه
elif page ==9 :
    st.markdown(
        "<h1 style='direction:rtl; text-align:right; color:black;'>مجمع نقية</h1>",
        unsafe_allow_html=True
    )

    html_text1 = """مجمع نيقية انعقد سنة 325م بسبب بدعة آريوس اللي أنكر مساواة الابن للآب. البابا ألكسندروس حضر ومعاه شماسه أثناسيوس الشاب اللي كان لسه في العشرينات لكنه كان قوي جدًا في الدفاع عن الإيمان. اجتمع 318 أسقف من كل العالم، وحضر آريوس وأتباعه."""
    html_text2 ="""في الجلسة الأولى حاول آريوس يشرح فكرته إن الابن مخلوق وليس من جوهر الآب، لكن الأساقفة ثاروا عليه. قام أثناسيوس ورد عليه بحجج كتابية قوية وأقنع الأغلبية بإضافة كلمة "هوموأوسيون" أي "مساوي للآب في الجوهر". اتفق المجمع على قانون الإيمان المعروف وحرَم آريوس وأتباعه ونفاه الملك قسطنطين وأمر بحرق كتبه.كمان المجمع رفض بدعة سابليوس اللي كان بيقول إن الآب والابن والروح القدس أقنوم واحد، وأصدر 20 قانون كنسي نظموا أمور زي تحديد ميعاد عيد القيامة، معمودية الهراطقة، وزواج الكهنة.وكان عدد الآباء 318، لكنهم كانوا دايمًا يلاقوا العدد يزيد بواحد، واعتبروا إن الروح القدس حاضر معاهم في المجمع."""
    col_img, col_text = st.columns([1, 2])
    with col_img:
        st.image("mgma10.jpg", width=400)
    with col_text:
        st.markdown(
            f"<p style='font-size:28px; line-height:1.9; direction:rtl; text-align:right; color:black;'>{html_text1}</p>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<p style='font-size:28px; line-height:1.9; direction:rtl; text-align:right; color:black;'>{html_text2}</p>",
            unsafe_allow_html=True
        )
        st.markdown(
        """
        <div style='text-align:left; margin-top:50px; margin-left:-480px;'>
        <a href="?page=2" target="_self">
            <button style='font-size:20px; padding:10px 25px; background-color:#f44336; color:black; border:none; border-radius:8px; cursor:pointer;'>
                رجوع
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
# -------------------------------------------------------------------  
#Contact Us
elif page ==10:
    st.markdown(
        "<h1 style='direction:rtl; text-align:right; color:black;'>Contact Us<h1>",
        unsafe_allow_html=True
    )
    html_text1 =""" لو عندك أي أسئلة أو اقتراحات، ممكن تتواصل معنا على:
    <br>البريد الإلكتروني: mekhailsaber905@gmail.com
    <br>رقم الهاتف: 01025323507
    </p>"""
    st.markdown(
            f"<p style='font-size:28px; line-height:1.9; direction:rtl; text-align:right; color:black;'>{html_text1}</p>",
            unsafe_allow_html=True)
# -------------------------------------------------------------------
#About Us
elif page ==11:
    st.markdown(
        "<h1 style='direction:rtl; text-align:right; color:black;'>About Us<h1>",
        unsafe_allow_html=True
    )
    html_text1 ="""انا ميخائيل صابر في الصف السادس مهتم بتقديم محتوى تعليمي وترفيهي مميز للأطفال والشباب 
    هدفي نشر المعرفة بطريقة ممتعة وتفاعلية، مع مراعاة القيم الروحية والتعليمية."""
    st.markdown(
            f"<p style='font-size:28px; line-height:1.9; direction:rtl; text-align:right; color:black;'>{html_text1}</p>",
            unsafe_allow_html=True)

