module.exports = {
  entry: __dirname + "/src/index.js",
  output: {
    filename: 'main.js',
    path: __dirname + "/dist/",
    assetModuleFilename: 'assets/[hash][ext][query]'
  },
  mode: process.env.NODE_ENV.trim(),
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: ["/node_modules/"],
        use: [
          {
            loader: "babel-loader",
            options: {
              presets: ["@babel/env"],
            },
          },
        ],
      },
      {
        test: /\.css$/,
        use: [
          "style-loader",
          "css-loader",
        ],
      },
      {
        test: /\.(png|svg|jpg|jpeg|gif)$/i,
        type: 'asset/resource',
      },
      {
        test: /\.(woff|woff2|eot|ttf|otf)$/i,
        type: 'asset/resource',
      },
    ]
  }
}