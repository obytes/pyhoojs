

task :hw do
  sh "echo 'Hello World!'"
end


task :test do
  sh "PYTHONPATH=. pytest"
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
end

task :clean_logs do
  sh "rm *.log -rf"
  sh "rm .firefox.log -rf"
end

task :clean => [:clean_pyc, :clean_screenshots, :clean_cache, :clean_logs] do
  puts "Ready for the day!"
end
