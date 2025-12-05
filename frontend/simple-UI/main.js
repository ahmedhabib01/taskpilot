const API = 'http://localhost:8000'
let token = ''

async function post(path, body){
  const res = await fetch(API+path, {
    method: 'POST',
    headers: { 
      'Content-Type': 'application/json', 
      ...(token?{Authorization:'Bearer '+token}: {}) 
    },
    body: JSON.stringify(body)
  })
  return res.json()
}

async function get(path){
  const res = await fetch(API+path, { 
    headers: token?{Authorization:'Bearer '+token}: {} 
  })
  return res.json()
}

document.getElementById('register').onclick = async ()=>{
  const email = document.getElementById('email').value
  const password = document.getElementById('password').value
  const r = await post('/users/register', { email, password })
  alert(JSON.stringify(r))
}

document.getElementById('login').onclick = async ()=>{
  const email = document.getElementById('email').value
  const password = document.getElementById('password').value
  const r = await post('/users/login', { email, password })
  token = r.access_token
  alert('Logged in')
}

document.getElementById('create').onclick = async ()=>{
  const title = document.getElementById('title').value
  const description = document.getElementById('description').value
  const r = await post('/tasks/', { title, description })
  alert(JSON.stringify(r))
  loadTasks()
}

async function loadTasks(){
  const tasks = await get('/tasks/')
  const ul = document.getElementById('tasks')
  ul.innerHTML = ''
  tasks.forEach(t=>{
    const li = document.createElement('li')
    li.textContent = t.title + ' - ' + (t.completed? 'done':'pending')
    ul.appendChild(li)
  })
}

loadTasks()
