/****************************
 * BABEL CONFIGURATION FILE
 * used for rollup babel plugin
 ***************************/

const development = process.env.ROLLUP_WATCH;

export default function (api) {
  return {
    parserOpts: { strictMode: true },
    presets: [
      // [
      //   "@babel/preset-env",
      //   {
      //     useBuiltIns: "usage", // alternative mode: "entry"
      //     corejs: 3, // default would be 2
      //     targets: "> 0.25%, not dead",
      //     // set your own target environment here (see Browserslist)
      //     // TODO: We want to configure this to reduce bundle size
      //     // targets: {
      //     // }
      //   },
      // ],

      [
        "@babel/preset-typescript",
        {
          // Remove type-only imports (introduced in TypeScript 3.8). This should only
          // be used if you are using TypeScript >= 3.8.
          onlyRemoveTypeImports: true,
        },
      ],
    ],
    plugins: [["@babel/plugin-proposal-class-properties", {}]],
    exclude: [/\/core-js\//],
  };
}
