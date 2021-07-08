const { series, parallel, src, dest, watch } = require("gulp");

const sass = require("gulp-dart-sass");
const imagenmin = require("gulp-imagemin");
const argv = require("yargs").argv;
const webp = require("gulp-webp");

// CSS
const autoprexifer = require("autoprefixer");
const postcss = require("gulp-postcss");
const cssnano = require("cssnano");
const sourcemap = require("gulp-sourcemaps");

// JS
// const terser = require("gulp-terser-js");
const gru2 = require("gulp-rollup-2");
const rollupOpts = require("./rollup.config");

const srcPath = "../src/frontend/static_src";
const srcPaths = {
  img: `${srcPath}/img/**/*`,
  scss: `${srcPath}/css/**/*.scss`,
  ts: `${srcPath}/js/**/*.ts`,
};

const dstPath = "../src/static";
const dstPaths = {
  img: `${dstPath}/img`,
  scss: `${dstPath}/css`,
  ts: `${dstPath}/js`,
};

function css() {
  return (
    src(srcPaths.scss)
      .pipe(sourcemap.init())
      .pipe(sass())
      .pipe(postcss([autoprexifer(), cssnano()]))
      // Map to original source
      .pipe(sourcemap.write("."))
      .pipe(dest(dstPaths.scss))
  );
}

async function javascript() {
  return (await gru2.src(...rollupOpts))
    .pipe(sourcemap.write("."))
    .pipe(dest(dstPaths.ts));
}

function optimizeImages() {
  return src(srcPaths.img).pipe(imagenmin()).pipe(dest(dstPaths.img));
  // .pipe(notify({ message: 'Imagen Minificada' }));
}

function versionWebp() {
  return src(srcPaths.img).pipe(webp()).pipe(dest(dstPaths.img));
}

function watchFilesJs() {
  watch(srcPaths.ts, javascript);
}

function watchFilesCss() {
  watch(srcPaths.scss, css);
}

exports.build_js = javascript;
exports.build_css = css;
exports.js = watchFilesJs;
exports.css = watchFilesCss;
exports.images = series(optimizeImages, versionWebp);
exports.default = parallel(
  css,
  javascript,
  versionWebp,
  watchFilesJs,
  watchFilesCss
);
