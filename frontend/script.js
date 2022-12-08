function setSendRequest(id, url, redirect) {
    $(id).on('submit', function(ev) {
        ev.preventDefault();
        let formData = new FormData(this);
        
        fetch(url, {
            method: 'POST',
            body: formData,
            credentials: 'include'
        })
        .then(
            (result) => {
                eval(redirect)
            },
    
            (err) => {
                alert("AAAAAAAAAAAAAAAA")
            }
        )
    })
}
