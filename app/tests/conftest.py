from app.main import create_app
import pytest


@pytest.fixture
def app():
    app = create_app()
    return app