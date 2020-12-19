import bodyParser from 'body-parser'
import express from 'express'
import session from 'express-session'

import * as sapper from '@sapper/server';

import authRoutes from './routers/auth'
import userRoutes from './routers/userActions'

const { PORT, NODE_ENV } = process.env;
const dev = NODE_ENV === 'development';

const app = express()

app.use(session({
    secret: 'stealthisifuwant',
    resave: true,
    saveUninitialized: true
}))

app.use(bodyParser.urlencoded({
    extended: true
}))

app.use(bodyParser.json())


app.use(express.static('static'))

app.use('/', authRoutes)
app.use('/', userRoutes)

app.use(sapper.middleware({
    session: (req, res) => {
        res.setHeader('cache-control', 'no-cache, no-store')
        const sessionObj = {
            email: req.session.email,
            key: req.session.key,
            mentor_recs: req.session.mentor_recs,

        }
        req.session.error = undefined
        return sessionObj
    }
}))
app.listen({ port: PORT },
    () => console.log(`Server ready at http://localhost:${PORT}`)
)