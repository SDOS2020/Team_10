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
    // const { slug } = req.params;
    const response = await post('api/class/', req.body, req.session.key)
    // console.log(response)
    const uuid = response['uuid']
    res.redirect(`/class/${response['uuid']}.svelte`)
})

router.post('/addPost/', async(req, res, next) => {
    // const { slug } = req.params;
    const {postText, classId} = req.body;
    const response = await post('api/class/post/', req.body, req.session.key)
    // console.log("text: " + response['postText'])
    // console.log("addPost " + response['classId'])
    // const uuid = response['classId']
    console.log(classId)
    res.redirect(`/class/${classId}.svelte`)
})

// router.get('/classDetails/', async(req, res, next) => {
//     const response = await get('api/class/', req.session.key)
//     const json = await response.json();
//     // console.log(response)
//     return json;

// })

router.get('/classDetails/', async(req, res, next) => {
    console.log(req.session.key)

    const response = await fetch(`${baseUrl}api/class/`, {
        method: 'GET',
        headers: {
            'Authorization': `Token ${req.session.key}`
        }
    })
    const json = await response.json()
    return res.json(json)
})


export default router;