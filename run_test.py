import pytest

if __name__ == "__main__":
    result = pytest.main([
        "tests/",           # папка с тестами
        "-q",               # тихий вывод (только результаты)
        "-ra",              # показать причины skipped/xfailed
        "--maxfail=1",      # остановка после первой ошибки
        "--disable-warnings",  # можно убрать или заменить на "-p no:warnings"
    ])

    if result == 0:
        print("\n✅ Все тесты успешно прошли!")
    else:
        print("\n❌ Некоторые тесты упали.")
