import gulp from 'gulp';
// import gulpSass from 'gulp-sass';
import modernizr from 'modernizr';
import autoprefixer from 'gulp-autoprefixer';
import sassGlob from 'gulp-sass-glob';
// import glob from 'glob';
import { deleteAsync as del } from 'del';
import nunjucksRender from 'gulp-nunjucks-render';
import browserSync from 'browser-sync';
import plumber from 'gulp-plumber';
import svgSprite from 'gulp-svg-sprite';
import prettyUrl from 'gulp-pretty-url';
import data from 'gulp-data';
// import rename from 'gulp-rename';
// import uglify from 'gulp-uglify';
// import filelist from 'gulp-filelist';
import { rollup } from 'rollup';
// import source from 'vinyl-source-stream';
// import buffer from 'vinyl-buffer';
import sourcemaps from 'gulp-sourcemaps';
import { babel } from '@rollup/plugin-babel';
import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import terser from '@rollup/plugin-terser';
import { createRequire } from 'module';

const require = createRequire(import.meta.url);
const sass = require('gulp-sass')(require('sass'));
const fs = require('fs');

const rollupConfig = {
  input: './assets/js/app.js',
  output: {
    file: './public/assets/js/app.bundle.js',
    format: 'iife',
  },
  plugins: [
    babel({
      babelHelpers: 'bundled',
      presets: ['@babel/preset-env'],
      babelrc: false,
      exclude: 'node_modules/**',
    }),
    resolve(),
    commonjs(),
    terser(),
  ],
};

const rollupJS = () => {
  return () => {
    return rollup(rollupConfig).then((bundle) => {
      return bundle.write({
        file: rollupConfig.output.file,
        format: rollupConfig.output.format,
        sourcemap: true,
      });
    });
  };
};

// --------------------------------

// Concat and copy CSS
gulp.task('scss', function (done) {
  gulp
    .src('assets/scss/**/*.scss')
    .pipe(plumber())
    .pipe(sassGlob())
    .pipe(sourcemaps.init())
    .pipe(sass({ outputStyle: 'compressed' }))
    .pipe(
      autoprefixer({
        grid: 'true',
      }),
    )
    .pipe(sourcemaps.write('.'))
    .pipe(gulp.dest('public/assets/css/'));
  done();
});

// Copy javascript
gulp.task('js', rollupJS());

gulp.task('modernizr', function (done) {
  modernizr.build(
    {
      // Add your Modernizr options here
      options: ['setClasses', 'addTest', 'testProp'],
      // Optionally add feature tests
      'feature-detects': ['touchevents', 'history'],
    },
    function (result) {
      fs.writeFileSync('assets/js/libs/modernizr.js', result);
      done();
    },
  );
});

// Assets copy
gulp.task('assets', function (done) {
  gulp.src(['assets/**/*', '!assets/scss/**/*']).pipe(plumber()).pipe(gulp.dest('public/assets/'));
  done();
});

// Copy Icons
gulp.task('icons', function (done) {
  gulp.src('assets/icons/**/*').pipe(plumber()).pipe(gulp.dest('public/assets/icons/'));
  done();
});

// Copy Icons
gulp.task('iconsprite', function (done) {
  gulp.src('assets/svg/icons/renders/*').pipe(plumber()).pipe(gulp.dest('public/assets/svg/icons/renders'));
  done();
});

// Copy CNAME
gulp.task('cname', function (done) {
  gulp
    .src(['./cname/CNAME']) // Source file
    .pipe(gulp.dest('./public')); // Output
  done();
});

// Copy Favicon
gulp.task('favicons', function (done) {
  gulp.src('assets/favicons/**/*').pipe(plumber()).pipe(gulp.dest('public/assets/favicons/'));
  done();
});

// Delete folders
gulp.task('cleanup', function () {
  return del(['public/**/*']);
});

// SVG Config
var config = {
  shape: {
    id: {
      separator: '-',
      whitespace: '-',
    },
  },
  mode: {
    symbol: {
      // symbol mode to build the SVG
      dest: 'assets/svg/icons/renders',
      sprite: 'sprite.svg',
      example: true,
      dimensions: '-svg',
      prefix: '.icon-',
    },
  },
  svg: {
    namespaceIDs: false,
    dimensionAttributes: false,
    xmlDeclaration: false, // strip out the XML attribute
    doctypeDeclaration: false, // don't include the !DOCTYPE declaration
  },
};

gulp.task('sprite-page', function (done) {
  gulp.src('assets/svg/icons/**/*.svg').pipe(plumber()).pipe(svgSprite(config)).pipe(gulp.dest('.'));
  done();
});

gulp.task('sprite-shortcut', function (done) {
  gulp.src('assets/svg/icons/renders/*').pipe(plumber()).pipe(gulp.dest('templates/'));
  done();
});

// --------------------------------------
// Templates
// --------------------------------------

// Render templates
gulp.task('render', function (done) {
  gulp
    .src(['templates/**/*.html', '!templates/00-guide/**/*.html', '!templates/layouts/**/*.html'])
    .pipe(plumber())
    .pipe(
      data(function () {
        return JSON.parse(fs.readFileSync('./models/data.json'));
      }),
    )
    .pipe(
      nunjucksRender({
        path: 'templates',
        inheritExtension: true,
      }),
    )
    .pipe(prettyUrl())
    .pipe(gulp.dest('public'));
  done();
});

// Watch more things
// gulp.task("watch-all", ["scss", "render", "icons", "svg", "favicons", "assets", "js", "sitemap", "guide", "cname"], function () {
gulp.task('watch-all', function () {
  gulp.watch('assets/js/**/*', gulp.series('js'));
  gulp.watch(['templates/**/*', 'models/**/*'], gulp.series('render'));
  gulp.watch('assets/scss/**/*', gulp.series('scss'));
  gulp.watch('assets/icons/**/*', gulp.series('icons'));
  gulp.watch('assets/favicons/*', gulp.series('favicons'));
  gulp.watch('cname/**/*', gulp.series('cname'));
});

// Spin up server
gulp.task('browser-sync', function (done) {
  browserSync.init({
    server: {
      baseDir: 'public',
    },
    notify: false,
    open: false,
    scrollProportionally: false,
    reloadDelay: 500,
    reloadDebounce: 500,
    scrollRestoreTechnique: 'cookie',
  });
  gulp.watch('public/**/*').on('change', browserSync.reload);
  done();
});

// --------------------------
// Task runners syntax
// --------------------------

// Just do a build
// gulp.task("default", ["render"]);

// Spins up a sever to render test templates
// gulp.task("serve", ["watch-all", "browser-sync"])
gulp.task(
  'serve',
  gulp.series('cleanup', 'scss', 'js', 'modernizr', 'assets', 'render', 'cname', 'browser-sync', 'watch-all'),
);

// Run a build
gulp.task(
  'build',
  gulp.series('cleanup', 'scss', 'js', 'icons', 'iconsprite', 'favicons', 'modernizr', 'assets', 'render', 'cname'),
);

// Icon Build
gulp.task('icons:build', gulp.parallel('sprite-page'));
