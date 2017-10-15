var gulp = require('gulp');
var shell = require('gulp-shell');
const files = ['dec.py'];

gulp.task('default', ['start', 'watch']);

gulp.task('start', shell.task(['python dec.py']));

gulp.task('watch', () => {
  return gulp.watch(files, ['start'])
});

gulp.task('reload', () => {
  gulp.src(files)
    .pipe(shell(['python dec.py']));
});