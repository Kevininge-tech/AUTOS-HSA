import streamlit as st
import pandas as pd

# Configurar la página
st.set_page_config(page_title="Registro de Autos", page_icon="🚗", layout="wide")

# Cargar el archivo
file_path = "REGISTRO DE AUTOS.xlsx"
xls = pd.ExcelFile(file_path)

# Estilos CSS
st.markdown("""
    <style>
        /* Estilos generales */
        body {background-color: #f4f4f4;}
        .stApp {background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);}
        .stTitle {color: #2E3B55; text-align: center;}
        
        /* Estilos para el sidebar */
        section[data-testid="stSidebar"] {
            background-color: #2E3B55 !important;
        }
        
        section[data-testid="stSidebar"] .stMarkdown p {
            color: white !important;
        }
        
        section[data-testid="stSidebar"] h1, 
        section[data-testid="stSidebar"] h2, 
        section[data-testid="stSidebar"] h3,
        section[data-testid="stSidebar"] label {
            color: white !important;
        }
        
        /* Estilo específico para el texto dentro del selectbox */
        section[data-testid="stSidebar"] select option,
        section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] span {
            color: black !important;
        }
        
        /* Estilos para la tabla */
        table {width: 100%; border-collapse: collapse;}
        th, td {border: 1px solid #ddd; padding: 8px;}
        th {background-color: #4CAF50; color: white; text-align: center !important; font-weight: bold;}
        td {text-align: left;}
        tr:nth-child(even) {background-color: #f2f2f2;}
    </style>
""", unsafe_allow_html=True)

# Selección de hoja
sheet_name = st.selectbox("Selecciona el año", xls.sheet_names)
df = pd.read_excel(xls, sheet_name=sheet_name)

# Lista de enlaces
enlaces_2024 = [
"https://drive.google.com/file/d/1JwXn3-pH4qBUw_sCxtSU_KDOmqhwmiDY/view?usp=drive_link",
"https://drive.google.com/file/d/1FQqBpVgxaJt3NNX60Dtjxxm_KOYpSIEb/view?usp=drive_link",
"https://drive.google.com/file/d/1Z66zwZh5POgTPcw3NQFLZ9-8ApnhODqk/view?usp=drive_link",
"https://drive.google.com/file/d/1oC2VjgQqopkBUP4BVI9oLfoEkD1lRpi8/view?usp=drive_link",
"https://drive.google.com/file/d/1uFr20tzzvFIS16u1LLJT8PgLdmeEd-AK/view?usp=drive_link",
"https://drive.google.com/file/d/1_F30NKZ_g9Cl5nD6GDB8irxnBYd2IIvF/view?usp=drive_link",
"https://drive.google.com/file/d/1mcYJQ14f0HrWwrfyAE2s3FjUvkKHd-lL/view?usp=drive_link",
"https://drive.google.com/file/d/1miRJpJ_PbFoSbf5Ts-0JkJHDsIl6oBXO/view?usp=drive_link",
"https://drive.google.com/file/d/1esJp1Da_s0-MKQcGww9_HNSq-MmGaQb0/view?usp=drive_link",
"https://drive.google.com/file/d/1zzoNf6fpH3EjmdT4NXF2nq_k-67A6jbU/view?usp=drive_link",
"https://drive.google.com/file/d/11GRZKuTvmSX1oa7i-THs4jwW3q6Ujb1B/view?usp=drive_link",
"https://drive.google.com/file/d/1GHq1krfdF5iUurOWVQEqqgue0eyfcqfP/view?usp=drive_link",
"https://drive.google.com/file/d/1TVus6ya9ZpVHA6xuCTfib_FLW-HiwmPb/view?usp=drive_link",
"https://drive.google.com/file/d/1SQhaxNr1zkfdp080nXT6vYAbIGba6m7l/view?usp=drive_link",
"https://drive.google.com/file/d/16ES536J-CLq_NZgozpmYmP99bo1RItOI/view?usp=drive_link",
"https://drive.google.com/file/d/1Y7C3_Dx7LjlQa-dvP4pAmBYHkxDmxB8F/view?usp=drive_link",
"https://drive.google.com/file/d/1f9BVNvzJmkHqQgbZsJOxLnpmu4Hg9eXV/view?usp=drive_link",
"https://drive.google.com/file/d/1K-wK_IZh2xv5SEtVEaBlvEGlHh6TNxuC/view?usp=drive_link", 
"https://drive.google.com/file/d/1t121jZmPYeebCM5mLrxslBD9FnsZ2u6L/view?usp=drive_link", 
"https://drive.google.com/file/d/1ajeYnySgl4jC191x6W4luYsjCfqq6Pb5/view?usp=drive_link",
"https://drive.google.com/file/d/16XhaqmAbKSyeRkiuRYG6FLdMXdQG3IW0/view?usp=drive_link",
"https://drive.google.com/file/d/1APo1KRXfh7k54CUUHrOwXOjtl0Mj9UIz/view?usp=drive_link",
"https://drive.google.com/file/d/1XsnT9u9OgNTXfWYiR6fzxmA1vtmOSc2U/view?usp=drive_link",
"https://drive.google.com/file/d/1EVeSD9mUF7tEDLSo_VQ9XVp77s34vVeq/view?usp=drive_link",
"https://drive.google.com/file/d/1ONlPnyonjUF2D2VHLrsp4RWAXVlmdlPZ/view?usp=drive_link",
"https://drive.google.com/file/d/1kjqzTSvDpBrlzRsX9m4Fd2qFjEygiPmk/view?usp=drive_link",
"https://drive.google.com/file/d/1RzNLXVT9FQzXXzq6m7Br01Mml73GuvuD/view?usp=drive_link",
"https://drive.google.com/file/d/1gFGtCiBfNSkIiSM5qMk3AD2VIZIkrLTq/view?usp=drive_link",
"https://drive.google.com/file/d/1x5I0bTud1VHwg2_k5IaDwT0tbwsWvlMb/view?usp=drive_link", 
"https://drive.google.com/file/d/1-TKZ3trRkdp_Lay7eutR6Ntl2piP3LFb/view?usp=drive_link",
"https://drive.google.com/file/d/1_Hro6-WesdFrbEfsZWFH2xm1Zw6b2xGm/view?usp=drive_link",
"https://drive.google.com/file/d/10mdUD3fHSPkW4_gCcNHSMde0qA7Jh6tu/view?usp=drive_link",
"https://drive.google.com/file/d/1j7BcloDLKfxXPIhPPiKLglnOcwTiIVBj/view?usp=drive_link",
"https://drive.google.com/file/d/1CI2T-__HjYFyX073plK-ThpwnRzyTpSU/view?usp=drive_link",
"https://drive.google.com/file/d/1fJC-7lzO-zXnYpaX0NP7SCfVPQ1A_yTy/view?usp=drive_link",
"https://drive.google.com/file/d/1rUN6VSB9VPcBnSqeQwIqrC4Sbk2uReWq/view?usp=drive_link",
"https://drive.google.com/file/d/1mYNS--3p5rd63PCPwRXmrwecDUBT5xrE/view?usp=drive_link",
"https://drive.google.com/file/d/1I1l_1jLV9lQBA2oMzTBcuSvvExJVMNf3/view?usp=drive_link",
"https://drive.google.com/file/d/1zaPA9qBNX6ENl3cKrXR2od0vZzDe9YTy/view?usp=drive_link",
"https://drive.google.com/file/d/1soA3L1EtzOhGSQnctBD-UzT4cXtEWoQ1/view?usp=drive_link",
"https://drive.google.com/file/d/117t6Llmm6KEpYBjDLYrhPfw7YY8Ck5Su/view?usp=drive_link",
"https://drive.google.com/file/d/1zuJ0ck5_ZltrKrSeYSA5M0AI5p42uuBj/view?usp=drive_link",
"https://drive.google.com/file/d/1qHDwgKT1Y7use8CoqNeBgo22WWl83S2w/view?usp=drive_link",
"https://drive.google.com/file/d/1HCJRifoMBcHccNMj2SQv-8681BQTK0JO/view?usp=drive_link",
"https://drive.google.com/file/d/1e9v7H4gHzQE8WqSEJnWLWw5di1g70u5A/view?usp=drive_link",
"https://drive.google.com/file/d/1mdaY3fGCaGyW1soxmxdQoGYdvNDXAEyi/view?usp=drive_link",
"https://drive.google.com/file/d/18-b2_F__WltPY9kI8a0ifG7dBzgRmAkn/view?usp=drive_link",
"https://drive.google.com/file/d/1KUUsTj_MvgH5nvJGIHpnm90J5blRmUQ5/view?usp=drive_link",
"https://drive.google.com/file/d/1esYiM53Ot0DTmML03XNuLiYKCfjfz4Jo/view?usp=drive_link",
"https://drive.google.com/file/d/1-lkyeQjcTYFpKPRK6uDRrX6L5bxPocpD/view?usp=drive_link",
"https://drive.google.com/file/d/1-aZaD0eL8HCWsxek1d-EOpf3dFGS-4Dq/view?usp=drive_link",
"https://drive.google.com/file/d/1TNOoFzE1S-W-x5B-NwlE1y12IVlDWMAc/view?usp=drive_link",
"https://drive.google.com/file/d/1zwoKaYd3jiwzg_mXZ2F9YauQEkedN4E-/view?usp=drive_link",
"https://drive.google.com/file/d/1Gp1X0DhRouSm_8tE2_yEpZVtASCgG8_W/view?usp=drive_link",
"https://drive.google.com/file/d/195ePCcxp15CyRToi7plwQo5nghorj8Uz/view?usp=drive_link",
"https://drive.google.com/file/d/1pz4CJkWDWH4LmXzVWcomR79MbsKK5VkU/view?usp=drive_link",
"https://drive.google.com/file/d/1W6NgQH2eyuXKi6ueNZbENqOTWZXaXyfm/view?usp=drive_link",
"https://drive.google.com/file/d/14bJnyCNV26pdfhPPUk737Ywt0AE1f4Mf/view?usp=drive_link",
"https://drive.google.com/file/d/1qgl49d1EdptfJlYM965BulvZJTo-bmu5/view?usp=drive_link",
"https://drive.google.com/file/d/1QoWdqZx6FXc_eOVYI__BrXJRxrEdlJcI/view?usp=drive_link",
"https://drive.google.com/file/d/1ieHRFsF8lGqqPL51DaOkjmf5Ey9qCvJv/view?usp=drive_link",
"https://drive.google.com/file/d/1zXBPAfbujoYzjYtr_okqbk18yyK4ztXC/view?usp=drive_link",
"https://drive.google.com/file/d/1e9do_QZY4HzhkS0lTZqfQxGXhF80f6I1/view?usp=drive_link",
"https://drive.google.com/file/d/11OxMJkL764PuJ37YcVyQRrDUExG7mSn8/view?usp=drive_link",
"https://drive.google.com/file/d/1J3NouCh2-JA32JFXswQ_z8iM5UmZHQji/view?usp=drive_link",
"https://drive.google.com/file/d/16yM0i4MG7nqZubHUtJClxGayj80t-XI_/view?usp=drive_link",
"https://drive.google.com/file/d/1rywvC2Bb7VBFR0f8OmfqrkT_ZrhMvU0h/view?usp=drive_link",
"https://drive.google.com/file/d/1SuubX522xZNYMu418YyonlwaSNCqypep/view?usp=drive_link",
"https://drive.google.com/file/d/1wRarhPaapT_gjboMZ7n3QlZZtA2R_rCb/view?usp=drive_link",
"https://drive.google.com/file/d/19bWFxVBbIcbgFlg43649IgoF0LD5pwSR/view?usp=drive_link",
"https://drive.google.com/file/d/1g5HnNWDcVd_iPMK1M0JrNcoYS7fn3w0z/view?usp=drive_link",
"https://drive.google.com/file/d/1Yhk3HW-u_QP-quKo892a21cEL75llBAL/view?usp=drive_link",
"https://drive.google.com/file/d/1ILELhRgUWL6G-RyVJmT4lu5GRuyYwe2u/view?usp=drive_link",
"https://drive.google.com/file/d/1Xz3idMaDBYhcNPu4jFb2-EXn_P4Z0XK0/view?usp=drive_link",
"https://drive.google.com/file/d/1YACtEofocA-Zjj1Q5V_wtjld5zvv7TJQ/view?usp=drive_link",
"https://drive.google.com/file/d/1d_rBGstqcYeTk9PEXyWA6-iIVw-SCvmP/view?usp=drive_link",
"https://drive.google.com/file/d/1YYLaFlA9dJzCVGOAWZt30VOM4pjWG9mt/view?usp=drive_link",
"https://drive.google.com/file/d/1fDViGhXRjgeb6AnI5_QZ1QfGzrkzfS0w/view?usp=drive_link",
"https://drive.google.com/file/d/1nqBmT6Mii1uErGjvwNA0EwD-V11W-Ky1/view?usp=drive_link",
"https://drive.google.com/file/d/1ziXpZUcntloBJATYiHMxf2KoH3Lp6MrS/view?usp=drive_link",
"https://drive.google.com/file/d/1YWwy4C8qVdUlvvxWrIR7rk46X5PtCrdy/view?usp=drive_link",
"https://drive.google.com/file/d/1YrnI7vYTdDpWCDkNeoLT9-zyqSoGKNx9/view?usp=drive_link",
"https://drive.google.com/file/d/1Dny6MN0UkmisnSwUGJW9AWZJfNYZB6fZ/view?usp=drive_link",
"https://drive.google.com/file/d/1MdfSL1i7VmgcxNamEYbPaRqLGyWVcU0f/view?usp=drive_link",
"https://drive.google.com/file/d/18rGLHEE2mZ0WjAZpRpaOz0ypt2nJdFms/view?usp=drive_link",
"https://drive.google.com/file/d/1N0BXA2v86jk8abIq9sxTWcrTNlkjbkKi/view?usp=drive_link",
"https://drive.google.com/file/d/1HABXnXadBcMRDu6L5oKQQO9aWfMY9yht/view?usp=drive_link",
"https://drive.google.com/file/d/1TlEueSgkX1I3WmK83O8nRY4eV1pqZNSK/view?usp=drive_link",
"https://drive.google.com/file/d/15UGxrWkhbOTFnr3r4JzmAjSIQ3nkA48g/view?usp=drive_link",
"https://drive.google.com/file/d/1IbKxZ-qHpEXt8Fy04CszL6OTa915xfjb/view?usp=drive_link",
"https://drive.google.com/file/d/1DWVzONuZvJ9253CBZSyuQDjl5I8VRs8h/view?usp=drive_link",
"https://drive.google.com/file/d/1A9apUJW27Hrt76RK0CUHci9mUfha28Fs/view?usp=drive_link",
"https://drive.google.com/file/d/1Ergb9vZoRTZlLIkde08Z5M0YkGDHx8g9/view?usp=drive_link",
"https://drive.google.com/file/d/1qu4H1rrH88Lq6U3nQt6LDv3AVwh_6LM7/view?usp=drive_link",
"https://drive.google.com/file/d/1dz8iuCB52y53f2ZJFxeOSHOkWjlND6C1/view?usp=drive_link",
"https://drive.google.com/file/d/13SMrzRam1Us5UoX-iXHR-cnJR4FIYDsq/view?usp=drive_link",
"https://drive.google.com/file/d/1vHJf1uY2jwOoxhTGv1Wl3Uf3cxd95YQG/view?usp=drive_link",
"https://drive.google.com/file/d/1sY01y4vEZUmxBq_tmrxUzNZI_ZOYG7Vw/view?usp=drive_link",
"https://drive.google.com/file/d/1_K7vdhEP2k52_PMC7jNabsBvVlQOXe9R/view?usp=drive_link",
"https://drive.google.com/file/d/1fXDT0NPYWgCpplfGPwehfHG2enQ6_5Jw/view?usp=drive_link",
"https://drive.google.com/file/d/1vl3F5pMel1inY0Th5kd1TJvZj_Pryhgl/view?usp=drive_link",
"https://drive.google.com/file/d/1axew9FpW1CvzgVhSUemrwId-wZlBTq8A/view?usp=drive_link",
"https://drive.google.com/file/d/11aGHYsyImAJyTrW3eU0BM1lqJGvFI_ov/view?usp=drive_link",
"https://drive.google.com/file/d/1z6ndtdm5zPxWna8zTWYaGueFouoqc8kp/view?usp=drive_link",
"https://drive.google.com/file/d/1IdvYaXttoKYERr8tewUjYNl56uyWqaFR/view?usp=drive_link",
"https://drive.google.com/file/d/1n_Cs_gMmo3Qimsvo_B0c89rMPm1PN6Xs/view?usp=drive_link",
"https://drive.google.com/file/d/1MxVf-u0KZoYMScfwL6ofOS3GEHSqNIpo/view?usp=drive_link",
"https://drive.google.com/file/d/1Q_HYqtRrlz4_88ABIlMn9B8_A8sqZ626/view?usp=drive_link",
"https://drive.google.com/file/d/1WcJ7yos_-04zwP5-pCNSmvnTREA7M4I8/view?usp=drive_link",
"https://drive.google.com/file/d/1Semj3M7le0ZmqqWabge7HebplymQu3AL/view?usp=drive_link",
"https://drive.google.com/file/d/1X2p_AX6RIUkp1L7YodJ_G8lfbYkDUIzZ/view?usp=drive_link",
"https://drive.google.com/file/d/1ADiC86CUr2RMfHK2CbNOy_XVI9T_w23E/view?usp=drive_link",
"https://drive.google.com/file/d/1EHNBcSOZncmNkO7MpavIfdSYYuvYOfkP/view?usp=drive_link",
"https://drive.google.com/file/d/1o-92ecGb2qvBJ7zBx8jgJlurjUTVi2UU/view?usp=drive_link",
"https://drive.google.com/file/d/1RtPyMTQo95jQkl2ad-eQLEmJhMQg8_4V/view?usp=drive_link",
"https://drive.google.com/file/d/1b5LyiYvcdwy_fliMpqfHss7bBsEHpEcI/view?usp=drive_link",
"https://drive.google.com/file/d/17UGJj0GBJDGNJ-VZbdU2gL5uYULyob9r/view?usp=drive_link",
"https://drive.google.com/file/d/1Y-GMDUl5q_kt9MaRJf9QJ9ANcOJQiWMD/view?usp=drive_link",
"https://drive.google.com/file/d/1FaIU7_aOpXZb1swb86numdpMcxoxjICd/view?usp=drive_link",
"https://drive.google.com/file/d/10x61xtNdie0TRyIo98Q07xFrK1gSi-W6/view?usp=drive_link",
"https://drive.google.com/file/d/1vYdtjHKoxZ8Nf8-0q2I8tLCywo2YS4vd/view?usp=drive_link",
"https://drive.google.com/file/d/1a9yYGV1Olc3z76yLn3e_TVQ2r5tY-2JO/view?usp=drive_link",
"https://drive.google.com/file/d/1lSIISNRj3F0rsEClkfU-EjVqyFpG4Zar/view?usp=drive_link",
"https://drive.google.com/file/d/1L4uCH7B4Hcn6dO--VZyRbcWJDpqKA1y5/view?usp=drive_link",
"https://drive.google.com/file/d/1D9Lr6SevilX1_5d7THPN5uOl20fPtpAw/view?usp=drive_link",
"https://drive.google.com/file/d/1vxfffDE19StTM_qSzMX3uDqloDUB0m0A/view?usp=drive_link",
"https://drive.google.com/file/d/1K7kSl2nvw9GjbgrmuFZT0B5Zp4_Ij-NQ/view?usp=drive_link",
"https://drive.google.com/file/d/154a5s_zak2V2Pb1QSBW3QB102MMVVHpt/view?usp=drive_link",
"https://drive.google.com/file/d/1AvlRbYSqls5y2wDfz6uE_WEdldK3hMVg/view?usp=drive_link",
"https://drive.google.com/file/d/1gke9iV65AFVs5Y5U_h6tQSMm9Jb26UI5/view?usp=drive_link",
"https://drive.google.com/file/d/1jByE7lLPpmadOQ9Xn3EmnZQl1iiwCny0/view?usp=drive_link",
"https://drive.google.com/file/d/1Z4EpQeU2XS8gLV8XGhqA2t-dfoSlqC5W/view?usp=drive_link",
"https://drive.google.com/file/d/1aPE34jtmEh2G9OWXn25ATYsF_6s1EEOm/view?usp=drive_link",
"https://drive.google.com/file/d/1YlIpZ6IKcfQSNlfKM6j1fzaMz8LeBcMY/view?usp=drive_link",
"https://drive.google.com/file/d/10xO7lfUR38vo8z8cbzfpNGMGt0gNrZa7/view?usp=drive_link",
"https://drive.google.com/file/d/1IW4G9Cqrom4DOcDnIgtZvJX2bCb4Z_W-/view?usp=drive_link",
"https://drive.google.com/file/d/1NhXyDJrqVLozPULPukdGd_abJOJVdVtg/view?usp=drive_link"
]

enlaces_2025 = [
"https://drive.google.com/file/d/12gJTnTtPViWT04bpRgMKTwIwzwkQQvCj/view?usp=drive_link",
"https://drive.google.com/file/d/12uu-I44o2FThMkq03N9f49BskdjHeJJf/view?usp=drive_link",
"https://drive.google.com/file/d/12vyfJlZrqmoowzb4KzGJQyWKxka6MuWy/view?usp=drive_link",
"https://drive.google.com/file/d/12wBe-HzlNPYpg2lDMHqYc5GhHV5F_cXb/view?usp=drive_link",
"https://drive.google.com/file/d/1UJ2pTvxALSJc7iQlSzz4ppT1wGlom1kt/view?usp=drive_link",
"https://drive.google.com/file/d/1Xq5-JGhZQ5RjZnHZXJ5i79dmVvpZMI6J/view?usp=drive_link",
"https://drive.google.com/file/d/1N9Vm3zEhf0u_3nJxzIuMUJv0x8543WUP/view?usp=drive_link",
"https://drive.google.com/file/d/1tjzxRblnn2RzM8kjW-AnNXdAFKv346m1/view?usp=drive_link",
"https://drive.google.com/file/d/1L2UKTySucQajQvhbUcix16uDH5fSxpPe/view?usp=drive_link",
"https://drive.google.com/file/d/1HsVLKw6cca3eFhtbI8tLIeA_PgLoDdJ4/view?usp=drive_link",
"https://drive.google.com/file/d/1w-HDJyhS6CZ74ppRempzHCnNHp7MjTlz/view?usp=drive_link",
"https://drive.google.com/file/d/1ECqW2f4PGSzSWSsUPVLHQSSruXlP1L0z/view?usp=drive_link",
"https://drive.google.com/file/d/1M1sYVYawUzO7k1dJu7RIs3ylSjGY3j_O/view?usp=drive_link",
"https://drive.google.com/file/d/1S1ZEYAwMGl6tNPmb3-SefRmSe8hyjstJ/view?usp=drive_link",
"https://drive.google.com/file/d/1bPUTULi37avTySwBESlAdf5MeNYQZgOh/view?usp=drive_link"

]
# Asignar enlaces según la hoja seleccionada
if sheet_name == "AUTOS 2024":
    if len(enlaces_2024) >= len(df):
        df["ENLACE"] = enlaces_2024[:len(df)]
    else:
        st.error("El número de enlaces para AUTOS 2024 no coincide con el número de registros.")
elif sheet_name == "AUTOS 2025":
    if len(enlaces_2025) >= len(df):
        df["ENLACE"] = enlaces_2025[:len(df)]
    else:
        st.error("El número de enlaces para AUTOS 2025 no coincide con el número de registros.")
else:
    df["ENLACE"] = ""

# Crear enlaces clickeables
df["ENLACE"] = df["ENLACE"].apply(lambda val: f'<a href="{val}" target="_blank" style="color: #1E88E5; text-decoration: none;">Ver Documento</a>' if pd.notnull(val) and val != "" else '')

# Interfaz con Streamlit
st.markdown(f"<h1 class='stTitle'>Registro de Autos {sheet_name}</h1>", unsafe_allow_html=True)

# Contenedor de filtros con diseño
with st.sidebar:
    st.header("Filtros 🔍")
    asesor = st.selectbox("Filtrar por Asesor", ["Todos"] + list(df["ASESOR"].dropna().unique()))
    asunto = st.selectbox("Filtrar por Asunto", ["Todos"] + list(df["ASUNTO"].dropna().unique()))

# Aplicar filtros
df_filtered = df.copy()
if asesor != "Todos":
    df_filtered = df_filtered[df_filtered["ASESOR"] == asesor]
if asunto != "Todos":
    df_filtered = df_filtered[df_filtered["ASUNTO"] == asunto]

# Mostrar tabla con enlaces clickeables
st.write("""<div style='border-radius: 10px; background-color: white; padding: 20px;'>""", unsafe_allow_html=True)
st.write(df_filtered.to_html(escape=False, index=False), unsafe_allow_html=True)
st.write("""</div>""", unsafe_allow_html=True)
