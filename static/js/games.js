$(document).ready(function () {
    $('#search-btn_game').on("click", function(e) {
        e.preventDefault();
        var searchText= $('#search-box_game').val();
            $.ajax({
                url:'/games?search_filter=' + searchText,
                type: 'GET',
                success: function(resp){
                var newHtml = resp.data.map(d =>{
                    return `<div class="well product">
                            <a class="product-link" href="/products/${d.id}">
                                <img class="product-img" src="${d.firstImage}"/>
                                <span class="product-name">${d.name}</span>
                                </a>
                                <span class="product-field"><strong>Price:</strong> ${d.price} USD</span>
                                <span class="product-field"><strong>Age Limit:</strong> ${d.age_limit} years</span>
                            </div>`
                });
                $('.products').html(newHtml.join(''));
                $('#search-box_game').val('');
            },
            error: function(xhr, status, error){
                    //TODO: show toestr
                console.error(error);
            }
        })
    });
});