var s = function(p) {

    p.setup = function() {
        var canvas = p.createCanvas(100, 100);
        p.background(255);
        p.cursor(p.CROSS);
    };

    p.draw = function() {

        // Is mouse over canvas?
        var mouseXInBounds = p.mouseX > 0 && p.mouseX < p.width;
        var mouseYInBounds = p.mouseY > 0 && p.mouseY < p.height;

        // Is the mouse pressed too?
        if (p.mouseIsPressed && mouseXInBounds && mouseYInBounds) {
            p.fill(0);
            p.noStroke();
            p.ellipse(p.mouseX, p.mouseY, 10, 10);
        }
    };

    p.randomiseCanvas = function() {

        p.drawRandomBackground();

        var complexity = 7;
        for (var i = 0; i < complexity; ++i) {

            if (p.random() < 0.4) {
                p.useRandomStroke();
            }

            if (p.random() < 0.4) {
                p.useRandomFill();
            }

            if (p.random() < 0.1) {
                p.useRandomRotation();
            }

            if (p.random() < 0.1) {
                p.useRandomMatrix();
            }

            if (p.random() < 0.1) {
                p.resetMatrix();
            }

            if (p.random() < 0.4) {
                p.drawRandomShape();
            }
        }
    };

    p.useRandomRotation = function() {
        p.rotate(p.random(p.TWO_PI));
    };

    p.useRandomMatrix = function() {
        p.applyMatrix(p.random(), p.random(), p.random(), p.random(), p.random(), p.random());
    };

    p.getRandomColour = function() {
        return p.color(p.random(256), p.random(256), p.random(256));
    };

    p.drawRandomBackground = function() {

        // Set background randomly.
        var backgroundColour = p.getRandomColour();
        p.fill(backgroundColour);
        p.noStroke();
        p.rect(0, 0, p.width, p.height);
    };

    p.useRandomStroke = function() {

        var strokeColour = p.getRandomColour();
        p.strokeWeight(p.random(10));
        p.stroke(strokeColour);
    };

    p.useRandomFill = function() {
        p.fill(p.getRandomColour());
    };

    p.drawRandomShape = function() {

        // Randomly choose from shape options.
        shapes = [
            'arc',
            'ellipse',
            'circle',
            'line',
            'point',
            'rect'
        ];
        var shape = p.random(shapes);

        // Draw random shape.
        if (shape == 'arc') {
            var s = p.random() * p.TWO_PI;
            var e = p.random() * p.TWO_PI;
            p.arc(p.random(), p.random(), p.random(), p.random(), s, e)

        } else if (shape == 'ellipse') {
            p.ellipse(p.random(100), p.random(100), p.random(100), p.random(100));

        } else if (shape == 'circle') {
            var r = p.random(100);
            p.ellipse(p.random(100), p.random(100), r, r);

        } else if (shape == 'line') {
            p.line(p.random(100), p.random(100), p.random(100), p.random(100));

        } else if (shape == 'point') {
            p.point(p.random(100), p.random(100));

        } else if (shape == 'rect') {
            p.rect(p.random(100), p.random(100), p.random(100), p.random(100));

        }
    };
};

var inputp5 = new p5(s, 'input-sketch-holder');
