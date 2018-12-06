from app.endpoints.user import UserAPI
from app.endpoints.event import EventAPI
from app.endpoints.event import EventMessagesAPI


def configure_views(app):
    # /users
    user_view = UserAPI.as_view('user_api')
    app.add_url_rule('/users', view_func=user_view)

    # /events
    event_view = EventAPI.as_view('event_api')
    app.add_url_rule(
        '/events/<event_id>',
        view_func=event_view,
        methods=['GET']
    )
    app.add_url_rule(
        '/events/',
        view_func=event_view,
        methods=['GET', 'POST']
    )
    app.add_url_rule(
        '/events/delete/<event_id>',
        view_func=event_view,
        methods=['DELETE']
    )
    # /events/messages
    event_msgs_view = EventMessagesAPI.as_view('event_msgs_view')
    app.add_url_rule(
        '/events/messages/<event_id>',
        view_func=event_msgs_view,
        methods=['GET']
    )
