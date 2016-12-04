task :hw do
  sh "echo 'Hello World!'"
end

desc "run unitest locally"
task :test => [:clean] do
  sh "PYTHONPATH=. py.test -s "
end

task :clean_pyc do
  sh "rm *.pyc -rf"
  sh "rm tests/*.pyc -rf"
end

task :clean_screenshots do
  sh "rm screenshot/*.png -rf"
end

task :clean_cache do
  sh "rm .cache/* -rf"
  sh "rm tests/__pycache__ -rf"
end

task :clean_logs do
  sh "rm *.log -rf"
  sh "rm .firefox.log -rf"
end

desc "clean pyc, screenshots, cache, logs, node_modules"
task :clean => [:clean_pyc, :clean_screenshots, :clean_cache, :clean_logs] do
  puts "Ready for the day!"
end

desc "build docker image"
task :build do
  sh "docker build -t chenglongzq/pyhoojs ."
end

desc "push docker image to dockerhub"
task :push => [:clean, :build] do
  sh "docker push chenglongzq/pyhoojs"
end

desc "run docker and get a terminal"
task :run do
  sh "docker run -it chenglongzq/pyhoojs /bin/bash"
end

desc "run unit test within docker"
task :dtest => [:clean] do
  sh "docker run chenglongzq/pyhoojs rake test"
end
