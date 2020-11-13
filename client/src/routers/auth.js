import express from 'express'
import fetch from 'node-fetch'

const router = express.Router()

const baseUrl = 'http://localhost:8000/'

async function post(endpoint, data, token = "") {
    const url = `${baseUrl}${endpoint}`

    const options = {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Token: ' + token
        }
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
    const response = await post('auth/users/', { first_name, email, password });

    console.log(response);

    res.redirect('/');
})

router.post('/login/', async(req, res, next) => {
    const { email, password } = req.body;
    const response = await post('auth/token/login/', { email, password });

    if ("auth_token" in response) {
        console.log("successful login" + response.auth_token)
        req.session.key = response.auth_token
    } else {
        // handle errors here
    }
    console.log(response);
    res.redirect('/')
})

router.get('/authtoken_check/', async(req, res, next) => {
    console.log(req.session.key)
    res.redirect('/')
})
router.get('/logout/', async(req, res, next) => {

    const options = {
        method: 'POST',
        headers: { 'Authorization': `Token ${req.session.key}` }
    }

    const response = await fetch('http://localhost:8000/auth/token/logout', options)


    req.session.destroy()
    res.redirect('/login/')
})
export default router