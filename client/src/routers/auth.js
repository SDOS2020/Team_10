import express from 'express'
import fetch from 'node-fetch'

const router = express.Router()

const baseUrl = 'http://localhost:8000/'

async function post(endpoint, data) {
    const url = `${baseUrl}${endpoint}`

    const options = {
        method: 'POST',
        body: JSON.stringify(data),
        headers: { 'Content-Type': 'application/json' }
    }

    const res = await fetch(url, options)
    const json = await res.json();

    return json;
}
async function get(endpoint) {
    const url = `${baseUrl}/${endpoint}/`
    await fetch(url)
}
router.post('/register/', async(req, res, next) => {
    const { first_name, email, password } = req.body;
    const response = await post('auth/users/', { first_name, email, password })

    console.log(response)

    res.redirect('/')
})

export default router