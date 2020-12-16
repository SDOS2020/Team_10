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

async function noAuthPost(endpoint, data, token = "") {
    const url = `${baseUrl}${endpoint}`
    const options = {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
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



router.post('/register/', async(req, res, next) => {
    const { first_name, email, password } = req.body;
    const response = await noAuthPost('auth/users/', { first_name, email, password });

    console.log(response);

    res.redirect('/');
})

router.post('/login/', async(req, res, next) => {
    const { email, password } = req.body;
    const response = await noAuthPost('auth/token/login/', { email, password });

    if ("auth_token" in response) {
        // fetch user details -> store to session
        console.log("successful login" + response.auth_token)

        req.session.key = response.auth_token

    } else {
        // handle errors here
    }
    console.log(response);
    res.redirect('/profile/')
})

router.post('/formtest/', async(req, res, next) => {
    const { projectname, projecttext } = req.body;
    console.log(projectname);
    console.log(projecttext);
})

router.get('/authtoken_check/', async(req, res, next) => {
    console.log(req.session.key || "lol")
    res.redirect('/')
})

router.get('/profileDetails/', async(req, res, next) => {
    console.log(req.session.key)

    const response = await fetch(`${baseUrl}api/user`, {
        method: 'GET',
        headers: {
            'Authorization': `Token ${req.session.key}`
        }
    })
    const json = await response.json()
    return res.json(json)
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


router.post('/completeProfile/', async(req, res, next) => {
    const response = await post('api/user/complete', req.body, req.session.key)

    console.log(response)
    res.redirect('/profile/complete')
})
export default router