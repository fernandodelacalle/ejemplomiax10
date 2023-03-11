from api_handler import BMEApiHandler
from eq_w import EqwAlgo


def handler(event, context):
    # Llamar al algo
    try:
        eq_w_1 = EqwAlgo(algo_tag='test_user_1_miax10_algo1', n_days=10)
        eq_w_1.run_day_comp()
    except Exception as e:
        print(f"Error en algo 1 {e}")

    try:
        eq_w_2 = EqwAlgo(algo_tag='test_user_1_miax10_algo2', n_days=20)
        eq_w_2.run_day_comp()
    except Exception as e:
        print(f"Error en algo 2 {e}")

    try:
        eq_w_3 = EqwAlgo(algo_tag='test_user_1_miax10_algo3', n_days=30)
        eq_w_3.run_day_comp()
    except Exception as e:
        print(f"Error en algo 3 {e}")
