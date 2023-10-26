/* eslint-disable @typescript-eslint/no-var-requires */
const path = require('path');
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');

module.exports = [
  {
    entry: {
      common: './src/common/index.ts',
    },
    output: {
      path: path.resolve(__dirname, './src/assets/'),
      filename: '[name]/js/bundle.js',
      publicPath: '/static/',
      chunkFilename: (pathData) => {
        const { runtime: name } = pathData.chunk;

        return `${name}/js/[chunkhash].bundle.js`;
      },
    },
    target: 'web',
    mode: 'development',
    watch: true,
    resolve: {
      extensions: ['.js', '.jsx', '.json', '.ts', '.tsx'],
    },
    module: {
      rules: [
        {
          test: /\.(ts|tsx)$/,
          loader: 'babel-loader',
        },
        {
          enforce: 'pre',
          test: /\.js$/,
          use: [
            {
              loader: 'source-map-loader',
              options: {
                filterSourceMappingUrl: (url, resourcePath) => {
                  // exclude react-image which results in an error
                  if (resourcePath.includes('node_modules/react-image/umd/index.js')) {
                    return false;
                  }

                  return true;
                },
              },
            },
          ],
        },
        {
          test: /\.css$/,
          use: ['style-loader', 'css-loader'],
        },
      ],
    },
    optimization: {
      minimizer: [`...`, new CssMinimizerPlugin()],
    },
    devtool: 'eval-source-map',
    externals: {
      jquery: 'jQuery',
    },
  },
];
