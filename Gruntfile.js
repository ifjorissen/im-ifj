module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    imifj: {
      app: 'im-ifj_static',
      build: 'static/im-ifj',
      tmp: 'staticfiles/im-ifj',
      sassDir: [
        '<%= imifj.app %>/sass'
      ],
      jsDir: [
        '<%= imifj.app %>/js'
      ],
    },
    blog: {
      build: 'static/blog',
      tmp: 'staticfiles/blog/',
      jsDir: [
        '<%= blog.build %>/js'
      ],
      cssDir: [
        '<%= blog.build %>/css'
      ],
    },
    playground: {
      build: 'static/playground',
      tmp: 'staticfiles/playground',
      jsDir: [
        '<%= playground.build %>/js'
      ],
      cssDir: [
        '<%= playground.build %>/css'
      ],
    },
    sass: {
          dev: {
            files: {
              '<%= imifj.build %>/css/main.css': '<%= imifj.sassDir %>/pages.scss',
              '<%= blog.build %>/css/main.css': '<%= imifj.sassDir %>/blog.scss',
              '<%= playground.build %>/css/main.css': '<%= imifj.sassDir %>/playground.scss',
              '<%= imifj.tmp %>/css/main.css': '<%= imifj.sassDir %>/pages.scss',
              '<%= blog.tmp %>/css/main.css': '<%= imifj.sassDir %>/blog.scss',
              '<%= playground.tmp %>/css/main.css': '<%= imifj.sassDir %>/playground.scss',
            }
          },
    },
    concat: {
            dev: {
              src: ['<%= imifj.app %>/js/*'],
              dest: '<%= imifj.build %>/js/app.min.js'
            },
    }, 
    watch: {
            options: {livereload: true},
            sass: {
                files: ['**/*.{scss,sass}'],
                tasks: ['sass']
            },
            javascript: {
                files: ['<%= imifj.jsDir %>/*'],
                tasks: ['concat:dev']
            }
            // sass: {
            //     files: ['<%= course.sassDir %>'],
            //     tasks: ['sass']
            // }
    },
    // Task configuration goes here.

  });

  // Load plugins here.
  grunt.loadNpmTasks('grunt-contrib-concat');
  // grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Register tasks here.
  grunt.registerTask('default', ['sass', 'concat', 'watch']);

};