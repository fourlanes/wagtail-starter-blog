'use strict';
/* eslint-disable @typescript-eslint/no-var-requires */
const { dest, series, src } = require('gulp');
const clean = require('gulp-clean');
const cleanCSS = require('gulp-clean-css');
const rename = require('gulp-rename');
const webpack = require('webpack');
const webpackStream = require('webpack-stream');
const { merge } = require('webpack-merge');
const webpackConfig = require('./webpack.config');

const webpackConfigProduction = webpackConfig.map((config) =>
  merge(config, {
    devtool: false,
    mode: 'production',
    watch: false,
  }),
);

function cleaning(cb) {
  ['src/assets/*'].forEach((_path) => {
    src(_path, { read: false }).pipe(clean());
  });

  cb();
}

function minifyCSS(cb) {
  src('./branding/assets/css/styles.css')
    .pipe(cleanCSS({ compatibility: 'ie8' }))
    .pipe(rename('styles.min.css'))
    .pipe(dest('./branding/assets/css/'));

  cb();
}

function streamWebpack(config) {
  if (typeof config.entry === 'object') {
    src(config.entry[Object.keys(config.entry)[0]]).pipe(webpackStream(config, webpack)).pipe(dest(config.output.path));
  } else {
    src(config.entry).pipe(webpackStream(config, webpack)).pipe(dest(config.output.path));
  }
}

function building(cb) {
  webpackConfigProduction.forEach(streamWebpack);

  cb();
}

function dev(cb) {
  webpackConfig.forEach(streamWebpack);

  cb();
}

exports.build = series(cleaning, building, minifyCSS);
exports.cssmin = minifyCSS;
exports.default = series(cleaning, dev);
