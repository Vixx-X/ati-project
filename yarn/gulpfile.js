const { series, parallel, src, dest, watch } = require("gulp"); // multiples funciones Importas lo que requires
const sass = require("gulp-dart-sass"); // una sola funcion
const imagenmin = require('gulp-imagemin');
const argv = require('yargs').argv;
// const notify = require('gulp-notify');
const webp = require("gulp-webp");
const concat = require("gulp-concat");

const gulp = require("gulp");
const typescript = require("gulp-typescript");

// Utilidades CSS
const autoprexifer = require("autoprefixer");
const postcss = require("gulp-postcss");
const cssnano = require("cssnano");
const sourcemap = require("gulp-sourcemaps");

// Utilidades JS
const terser = require("gulp-terser-js");
const rename = require("gulp-rename");

const paths = {
  imagenes: "../src/frontend/static_src/img/**/*",
  scss: "../src/frontend/static_bundle/css/**/*.scss",
  //js: 'src/js/**/*.js',
  ts: "../src/frontend/static_bundle/js/**/*.ts",
};

function css() {
  const isDev = (argv.dev === undefined) ? false : true;
  if( isDev ){
    return (
      src(paths.scss)
        .pipe(sourcemap.init())
        .pipe(sass())
        .pipe(postcss([autoprexifer(), cssnano()]))
        .pipe(sourcemap.write("."))
        .pipe(dest("../src/frontend/static/css"))
    );
  }else{
    return (
      src(paths.scss)
        .pipe(sass())
        .pipe(postcss([autoprexifer(), cssnano()]))
        .pipe(dest("../src/frontend/static/css"))
    );
  }
}

function javascript() {
  const isDev = (argv.dev === undefined) ? false : true;
  return (
    src(paths.ts)
      .pipe(
        typescript({
          noImplicitAny: true,
        })
      )
      .pipe(sourcemap.init())
      // .pipe(concat('bundle.js'))
      .pipe(terser())
      .pipe(sourcemap.write('.'))
      .pipe(dest("../src/frontend/static/js"))
  );
}

function imagenes() {
  return src(paths.imagenes)
      .pipe(imagenmin())
      .pipe(dest('../src/frontend/static/img'));
  // .pipe(notify({ message: 'Imagen Minificada' }));
}

function versionWebp() {
  return src(paths.imagenes)
    .pipe(webp())
    .pipe(dest("../src/frontend/static/img"));
}

function watchArchivosJs() {
  watch(paths.ts, javascript);
  // * = La carpeta actual
  // **/* = todos los archivos dentro de esa carpeta si importad en nivel de profundidad que tengan esa extension
}

function watchArchivosCss(){
  watch(paths.scss, css);
}


exports.build_js= javascript;
exports.build_css = css;
exports.js = watchArchivosJs;
exports.css = watchArchivosCss;
exports.images = series(imagenes, versionWebp);
exports.default = parallel(css, javascript, versionWebp, watchArchivosJs, watchArchivosCss);