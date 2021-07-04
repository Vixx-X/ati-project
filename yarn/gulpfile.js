const { series, src, dest, watch } = require('gulp'); // multiples funciones Importas lo que requires 
const sass = require('gulp-dart-sass'); // una sola funcion 
//const imagenmin = require('gulp-imagemin');
//const notify = require('gulp-notify');
const webp = require('gulp-webp');
const concat = require('gulp-concat');

const gulp = require('gulp');
const typescript = require('gulp-typescript');

//Utilidades CSS
const autoprexifer = require('autoprefixer');
const postcss = require('gulp-postcss');
const cssnano = require('cssnano');
const sourcemap = require('gulp-sourcemaps');

//Utilidades JS
const terser = require('gulp-terser-js');
const rename = require('gulp-rename');

const paths = {
    imagenes: '../src/frontend/static_src/img/**/*',
    scss: '../src/frontend/static_src/css/**/*.scss',
    //js: 'src/js/**/*.js',
    ts: '../src/frontend/static_src/js/**/*.ts'
}

function css() {
    return src(paths.scss)
        .pipe(sourcemap.init())
        .pipe(sass())
        .pipe(postcss([autoprexifer(), cssnano()]))
        //Para saber donde esta todo del codigo original
        .pipe(sourcemap.write('.'))
        .pipe(dest('../src/frontend/static/css'));
}

function javascript() {
    return src(paths.ts)
        .pipe(typescript({
            noImplicitAny: true,
            outFile: 'bundle.js'
        }))
        // .pipe(sourcemap.init())
        // .pipe(concat('bundle.js'))
        // .pipe(terser())
        // .pipe(sourcemap.write('.'))
        // .pipe(rename({ suffix: '.min' }))
        .pipe(dest('../src/frontend/static/js'));
}

function versionWebp() {
    return src(paths.imagenes)
        .pipe(webp())
        .pipe(dest('../src/frontend/static/img'));
}

function watchArchivos() {
    watch(paths.scss, css);
    watch(paths.ts, javascript);
    // * = La carpeta actual 
    // **/* = todos los archivos dentro de esa carpeta si importad en nivel de profundidad que tengan esa extension
}

exports.javascript = javascript;
exports.css = css;
exports.default = series(css, javascript, versionWebp, watchArchivos);