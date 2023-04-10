# 公共断言方法
def common_assert(case, response, status_code=200, code=20000, status="success"):
    case.assertEqual(status_code, response.status_code)
    case.assertEqual(code, response.json().get("code"))
    case.assertIn(status, response.json().get("status"))
