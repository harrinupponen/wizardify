//This reads the users uploaded image and sets it to be visible on screen 
$('#image-selector').change(function() {
    let reader = new FileReader();
    reader.onload = function() {
        let dataURL = reader.result;
        $('#selected-image').attr('src', dataURL);
        $('#prediction-list').empty();
    }
    let file = $('#image-selector').prop('files')[0];
    reader.readAsDataURL(file);
});

//This loads the model from set path
let model;
(async function() {
    model = await tf.loadLayersModel('./models/final_model/model.json');
    $('.progress-bar').hide();
})();

//This makes the prediction using user image and model
$('#predict-button').click(async function() {
    let image = $('#selected-image').get(0);
    let offset = tf.scalar(127.5);
    let tensor = tf.browser.fromPixels(image)
        .resizeNearestNeighbor([224, 224])
        .toFloat()
        .sub(offset)
        .div(offset)
        .expandDims();

    //This forms the prediction data, sorts it and prints the top 5 results on screen
    let predictions = await model.predict(tensor).data();
    let top5 = Array.from(predictions).map(function (p, i) {
            return {
                propability: p,
                className: DND_CLASSES[i]
            };
        }).sort(function (a, b) {
            return b.propability - a.propability;
        }).slice(0, 5);
    $('#prediction-list').empty();
    top5.forEach(function (p) {
        $('#prediction-list').append(`<li>${p.className}: ${(100 * (p.propability)).toFixed(2)} %</li>`);
    });
});

