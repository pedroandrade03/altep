const meuIntervalo = setInterval(function(){
        const formData = new FormData();
        formData.append('status', 'atualizar');
        return fetch('{% url 'att_registros' %}', {
            method: 'POST',
            body: formData,
            headers:  {
                "X-CSRFToken": '{{ csrf_token }}'
            }
        });
}, 15000);