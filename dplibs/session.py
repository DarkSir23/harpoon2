from django.contrib.sessions.models import Session
from django.utils import timezone

def clear_inactive_sessions():
    inactive_sessions = Session.objects.filter(expire_date__lt=timezone.now())
    inactive_sessions.delete()

def get_sessions(userid=None):
    from users.models import CustomUser
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_sessions = []
    all_sessions = {}
    for session in active_sessions:
        data = session.get_decoded()
        session_info = {'expire_date': session.expire_date, 'session_key': session.session_key}
        sessionuserid = data.get('_auth_user_id', None)
        for key in data.keys():
            session_info[key] = data[key]
        if userid and str(userid) == sessionuserid:
            user_sessions.append(session_info)
        elif userid:
            pass
        elif sessionuserid:
            user = CustomUser.objects.get(pk=int(sessionuserid))
            session_info['user'] = user
            if user.id in all_sessions.keys():
                all_sessions[user.id].append(session_info)
            else:
                all_sessions[user.id] = [session_info]
    if userid:
        return user_sessions
    else:
        return all_sessions



