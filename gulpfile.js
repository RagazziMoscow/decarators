var gulp = require('gulp');
var shell = require('gulp-shell');
const files = ['decorators.py', 'functions.py'];

gulp.task('default', ['start', 'watch']);

gulp.task('start', shell.task([`python ${files[1]}`]));

gulp.task('watch', () => {
  return gulp.watch(files, ['start'])
});

gulp.task('reload', () => {
  gulp.src(files)
    .pipe(shell([`python ${files[1]}`]));
});