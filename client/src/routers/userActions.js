import express from 'express'
import fetch from 'node-fetch'
import { authCheck } from '../utils/user'
const router = express.Router()

const baseUrl = 'http://localhost:8000/'

async function post(endpoint, data, token = "") {
    const url = `${baseUrl}${endpoint}`
    const options = {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + token
        }
    }

    const res = await fetch(url, options)
    const json = await res.json();

    return json;
}

async function get(endpoint, token = "") {
    const url = `${baseUrl}${endpoint}`
    const options = {

        headers: {
            'Authorization': 'Token ' + token
        }
    }
    const res = await fetch(url, options);
    const json = await res.json();

    return json;
}

router.post('/applyMentor/', async(req, res, next) => {
    console.log(req.body)
    const response = await post('api/mentor/apply/', req.body, req.session.key)

    console.log(response)
    res.redirect('/mentoring/apply/')
})

router.post('/createClass/', async(req, res, next) => {
    const response = await post('api/class/', req.body, req.session.key)
    console.log(response)
    const uuid = 'index'
    res.redirect(`/class/${uuid}.svelte`)
})
export default router;