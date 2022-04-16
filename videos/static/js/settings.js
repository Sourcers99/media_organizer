var setting_forms = [...document.getElementsByClassName('setting-form')]
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
setting_forms.forEach(form => form.addEventListener('submit', e=>  {
    e.preventDefault()
    const form_id = e.target.getAttribute('data-form-id')
    const video_path = document.getElementById(`${form_id}`)
    params = JSON.stringify({
        id: form_id,
        settings : video_path.value
    })
    console.log(video_path)
    fetch('/save-settings/', {
        method: 'POST',
        body: params,
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
    }).then(response => response.json())
    .then(data => {
        video_path.value = ''
        console.log(data)
        console.log(params)
    })
    
}))
