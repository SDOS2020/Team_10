export function isLoggedIn(session) {
    return session.key
}

export function authCheck(session, redirect) {
    if (!isLoggedIn(session)) { redirect(302, '/login'); return false; } else {
        return true;
    }
}