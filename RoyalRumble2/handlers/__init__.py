from handlers import admin, help, history, leaderboard, match, moves, profile, rumble, start, tag

routers = [start.router, help.router, match.router, moves.router, profile.router,
           leaderboard.router, history.router, rumble.router, tag.router, admin.router]
