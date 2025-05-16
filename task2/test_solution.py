from task2.solution import get_animals_by_letter

def test_get_animals_by_letter(monkeypatch):
    # Мокаем requests.Session.get, чтобы не делать реальный запрос к API
    class MockSession:
        def __init__(self):
            self.calls = 0
        def get(self, url, params=None):
            self.calls += 1
            # Первый вызов возвращает первую порцию
            if self.calls == 1:
                return MockResp({
                    "query": {
                        "categorymembers": [
                            {"title": "Аист"},
                            {"title": "Бобр"},
                            {"title": "Акула"}
                        ]
                    },
                    "continue": {"cmcontinue": "page|123"}
                })
            # Второй вызов — последняя порция
            else:
                return MockResp({
                    "query": {
                        "categorymembers": [
                            {"title": "Барсук"}
                        ]
                    }
                })
    class MockResp:
        def __init__(self, data):
            self._data = data
        def json(self):
            return self._data
    monkeypatch.setattr('requests.Session', MockSession)
    result = get_animals_by_letter()
    assert result['А'] == 2
    assert result['Б'] == 2 