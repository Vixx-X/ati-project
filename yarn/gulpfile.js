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

function optimizeImages() {
  return src(srcPaths.img).pipe(imagenmin()).pipe(dest(dstPaths.img));
  // .pipe(notify({ message: 'Imagen Minificada' }));
}

function versionWebp() {
  return src(srcPaths.img).pipe(webp()).pipe(dest(dstPaths.img));
}

function watchFilesCss() {
  watch(srcPaths.scss, css);
}

exports.build_css = css;
exports.css = watchFilesCss;
exports.images = series(optimizeImages, versionWebp);
exports.default = parallel(css, versionWebp, watchFilesCss);
