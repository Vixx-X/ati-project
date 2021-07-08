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
const bundlePath = "../src/frontend/static_bundle";
const srcPaths = {
  img: `${srcPath}/img/**/*`,
  scss: `${bundlePath}/css/**/*.scss`,
};

const dstPath = "../src/static";
const dstPaths = {
  img: `${dstPath}/img`,
  scss: `${dstPath}/css`,
};

function css() {
  const isDev = argv.dev === undefined ? false : true;
  if (isDev) {
    return src(srcPaths.scss)
      .pipe(sourcemap.init())
      .pipe(sass())
      .pipe(postcss([autoprexifer(), cssnano()]))
      .pipe(sourcemap.write("."))
      .pipe(dest(dstPaths.scss));
  } else {
    return src(srcPaths.scss)
      .pipe(sass())
      .pipe(postcss([autoprexifer(), cssnano()]))
      .pipe(dest(dstPaths.scss));
  }
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
