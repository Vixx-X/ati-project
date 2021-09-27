const { series, parallel, src, dest, watch } = require("gulp");

const sass = require("gulp-dart-sass");
const argv = require("yargs").argv;

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
  let el = src(srcPaths.scss);
  if (argv.dev) {
    el = el.pipe(sourcemap.init());
  }
  el = el.pipe(sass()).pipe(postcss([autoprexifer(), cssnano()]));
  if (argv.dev) {
    el = el.pipe(sourcemap.write("."));
  }
  return el.pipe(dest(dstPaths.scss));
}

function watchFilesCss() {
  watch([srcPaths.scss, `${srcPath}/css/**/*.scss`], css);
}

// IMAGES
function versionWebp() {
  return src(srcPaths.img).pipe(dest(dstPaths.img));
}

exports.images = series(versionWebp);
exports.build_css = css;
exports.css = watchFilesCss;
exports.default = parallel(css, versionWebp, watchFilesCss);
