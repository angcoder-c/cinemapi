from main import app

test_app_get_public = app.test_client()
test_app_post_public = app.test_client()
test_app_get_private = app.test_client()
test_app_post_private = app.test_client()