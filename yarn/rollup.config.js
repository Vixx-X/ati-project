/****************************
 * ROLLUP CONFIGURATION FILE
 ***************************/

import path from "path";
import { terser } from "rollup-plugin-terser";
import { babel } from "@rollup/plugin-babel";
import commonjs from "@rollup/plugin-commonjs";
import { nodeResolve } from "@rollup/plugin-node-resolve";
import multiInput from "rollup-plugin-multi-input";
import includePaths from "rollup-plugin-includepaths";

const development = process.env.ROLLUP_WATCH;
const production = !development;

const baseExtensions = [".js", ".jsx", ".ts", ".tsx"];

// Import extensions to look for
const importExtensions = [...baseExtensions, ...[".mjs", ".json", ".node"]];

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

export default {
  input: [
    // Look for all typescript files in the bundle directory, courtesy of includePaths
    srcPaths.ts,
  ],

  // Specify here external modules which you don't want to include in your bundle (for instance: 'lodash', 'moment' etc.)
  // https://rollupjs.org/guide/en/#external
  external: [],

  // Disable treeshake if we are on development, to improve build speeds
  treeshake: production,
  output: {
    format: "esm", // Keep the bundle as an ES module file, suitable for other bundlers and inclusion as a <script type=module> tag in modern browsers
    plugins: [
      terser(), // minify the output
    ],

    dir: dstPaths.ts,
    // Appended source map to the resulting output file as a data URI
    sourcemap: development ? "inline" : false,
  },

  plugins: [
    // Allows rollup to use multiple entry points, input glob pattern
    // and preserve asset/js tree structure in the static folder.
    // multiInput({ relative: srcPath }),

    // Allows node_modules resolution
    nodeResolve({
      // Instructs the plugin to use the "browser" property in package.json
      browser: true,

      // Specify the extensions of files that the plugin will operate on.
      extensions: importExtensions,

      // Specifies the properties to scan within a package.json
      mainFields: ["browser", "jsnext:main", "module", "main"],
    }),

    // Allow relative paths in your import directives
    includePaths({
      paths: [paths.common],
      extensions: importExtensions,
    }),

    // Convert CommonJS modules to ES6, so they can be included in a Rollup bundle
    commonjs({
      // Skip source map generation for CommonJS modules. This will improve performance.
      sourceMap: false,
    }),

    // Compile typescript and convert future ECMASCRIPT features
    // to ECMASCRIPT supported by browsers

    babel({
      // === Plugin specific configuration === //
      // https://github.com/rollup/plugins/tree/master/packages/babel

      // An array of file extensions that Babel should transpile.
      extensions: [...baseExtensions, ...[".es6", ".es", ".mjs"]],

      // Recommended to configure this option explicitly,
      // Contain at most one copy of the helpers
      babelHelpers: "bundled",

      // === Babel specific configuration === //
      // https://babeljs.io/docs/en/options
      configFile: path.join(__dirname, "babel.config.mjs"),
    }),
  ],
};
